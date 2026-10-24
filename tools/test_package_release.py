"""Release contract checks against the actual edition assets and ZIPs."""
import copy
import re
import unittest
import zipfile
from package_release import ROOT, accepts_android, build, digest, edition_files, read_json, validate


class ReleaseTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest, cls.selection, cls.editions = validate()
        cls.report = build()

    def test_shared_fonts_match_reviewed_v06_without_badges(self):
        prior = read_json(ROOT/'docs/v0.6/verification.json')
        reference = {r['filename']:r['sha256'] for r in prior['files']
                     if '-A4CF47DD968DAA08-' not in r['filename']}
        self.assertEqual(reference, self.editions['fonts'])
        self.assertEqual(101,len(reference))

    def test_art_is_only_the_reviewed_optional_rectangles(self):
        optional = set(self.editions['ui-art'])-set(self.editions['fonts'])
        self.assertEqual(20,len(optional))
        self.assertEqual(2,sum('-A4CF47DD968DAA08-' in n for n in optional))
        self.assertEqual(1,sum('-A9FBF4E578AF475A-' in n for n in optional))
        for name, value in self.editions['fonts'].items():
            self.assertEqual(value,self.editions['ui-art'][name])

    def test_all_archives_have_exact_selected_assets(self):
        for record in self.report['archives']:
            with self.subTest(archive=record['name']), zipfile.ZipFile(ROOT/'release-assets'/record['name']) as z:
                self.assertIsNone(z.testzip())
                self.assertEqual(len(z.namelist()),len(set(z.namelist())))
                images = {n.rsplit('/',1)[-1]:digest(z.read(n)) for n in z.namelist() if n.endswith('.png')}
                self.assertEqual(self.editions[record['edition']],images)
                if record['platform']=='android':
                    self.assertEqual(len(images),len(z.namelist()))
                    self.assertTrue(all(accepts_android(n) for n in z.namelist()))
                else:
                    self.assertEqual(len(images)+2,len(z.namelist()))
                    self.assertTrue(all(n.startswith('SLUS-01040/') for n in z.namelist()))
                    self.assertIn(self.selection['editions'][record['edition']]['name'],z.read('SLUS-01040/ABOUT.txt').decode())

    def test_android_approval_does_not_carry_over_to_changed_payload(self):
        art = next(r for r in self.report['archives'] if r['edition']=='ui-art' and r['platform']=='android')
        device = self.manifest['android']
        if device['current_payload_device_tested']:
            self.assertEqual(device['tested_archive_sha256'],art['sha256'])
            self.assertEqual(device['tested_pack_fingerprint'],art['pack_fingerprint'])
        else:
            self.assertNotEqual(device['tested_pack_fingerprint'],art['pack_fingerprint'])
            self.assertFalse(self.manifest['badge_artwork']['android_tested'])

    def test_android_import_report_describes_current_payload(self):
        report = read_json(ROOT/'verification-android-import.json')
        self.assertEqual(self.manifest['pack_fingerprint'],report['pack_fingerprint'])
        self.assertEqual(self.manifest['pngs'],report['matching_texture_entries'])
        self.assertEqual(self.manifest['editions'],report['editions'])
        self.assertEqual(self.manifest['android']['current_payload_device_tested'],
                         report['current_payload_device_tested'])

    def test_badges_are_art_only_and_have_correct_category_mappings(self):
        record = read_json(ROOT/'docs/editing-records-v0.8.json')
        assets = {r['name']:r for r in record['assets']}
        expected = {'dagger':[80,96,16,16], 'sword':[144,96,16,16],
                    'great-sword':[160,96,16,16], 'polearm':[96,96,16,16],
                    'crossbow':[48,112,16,16], 'shield':[64,112,16,16],
                    'grips-category':[152,128,16,16], 'shield-category':[168,128,16,16]}
        for name, rect in expected.items():
            self.assertEqual(rect,assets[name]['native_rect'])
        for asset in assets.values():
            self.assertIn(asset['filename'],self.selection['groups']['ui-art'])
            self.assertNotIn(asset['filename'],self.editions['fonts'])
            self.assertEqual(asset['master_sha256'],digest((ROOT/asset['master']).read_bytes()))

    def test_edition_misclassification_is_rejected(self):
        wrong = copy.deepcopy(self.selection)
        body = next(n for n in wrong['groups']['ui-art'] if '-A9FBF4E578AF475A-' in n)
        wrong['groups']['ui-art'].remove(body)
        wrong['groups']['fonts'].append(body)
        with self.assertRaises(ValueError):
            edition_files(self.manifest,wrong)

    def test_missing_and_duplicated_assets_are_rejected(self):
        missing = copy.deepcopy(self.selection)
        missing['groups']['fonts'].pop()
        duplicate = copy.deepcopy(self.selection)
        duplicate['groups']['fonts'].append(duplicate['groups']['ui-art'][0])
        for wrong in (missing,duplicate):
            with self.assertRaises(ValueError):
                edition_files(self.manifest,wrong)

    def test_android_rejects_wrappers_nested_paths_and_settings(self):
        name = next(iter(self.editions['fonts']))
        good = 'textures/SLUS-01040/replacements/'+name
        self.assertTrue(accepts_android(good))
        for bad in ['Wrapper/'+good,good.removeprefix('textures/'),
                    'textures/SLUS-01040/config.yaml',
                    'textures/SLUS-01040/replacements/../'+name,
                    'textures/SLUS-01040/replacements/nested/'+name]:
            self.assertFalse(accepts_android(bad),bad)

    def test_switching_requires_removal_of_old_art(self):
        old_art = self.editions['ui-art']
        imported_fonts = dict(old_art,**self.editions['fonts'])
        self.assertEqual(121,len(imported_fonts))
        self.assertNotEqual(imported_fonts,self.editions['fonts'])
        for name in self.selection['groups']['ui-art']:
            imported_fonts.pop(name)
        self.assertEqual(imported_fonts,self.editions['fonts'])
        old_v06 = {r['filename']:r['sha256'] for r in read_json(ROOT/'docs/v0.6/verification.json')['files']}
        self.assertEqual(103,len(dict(old_v06,**self.editions['fonts'])))
        self.assertEqual(101,len(dict(self.editions['fonts'])))

    def test_readme_downloads_match_built_archives(self):
        text = (ROOT/'README.md').read_text(encoding='utf-8')
        links = re.findall(r'/releases/download/v'+re.escape(self.manifest['package_version'])+r'-beta/([^\s)]+\.zip)',text)
        self.assertEqual(sorted(r['name'] for r in self.report['archives']),sorted(links))

    def test_archive_build_is_deterministic(self):
        repeated = build()
        self.assertEqual(self.report['archives'],repeated['archives'])


if __name__ == '__main__':
    unittest.main()
