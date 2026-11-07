"""Keep release metadata and edition scope synchronized during the next bump."""
from contextlib import redirect_stdout
from datetime import date
from io import StringIO
from pathlib import Path
import json
import tempfile
import unittest
from unittest.mock import patch
import bump_version


class BumpTests(unittest.TestCase):
    def test_bump_preserves_current_edition_scope_and_refreshes_import_manifest(self):
        source = bump_version.ROOT
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            for name in ['verification.json','verification-android-import.json','editions.json',
                         'README.md','docs/INSTALL.md','textures/SLUS-01040/ABOUT.txt']:
                target = root/name
                target.parent.mkdir(parents=True,exist_ok=True)
                target.write_bytes((source/name).read_bytes())
            manifest = json.loads((root/'verification.json').read_text(encoding='utf-8'))
            selection = json.loads((root/'editions.json').read_text(encoding='utf-8'))
            selection['editions']['ui-art']['description'] = 'Same fonts, plus future reviewed menu artwork.'
            (root/'editions.json').write_text(json.dumps(selection),encoding='utf-8')
            # Simulate the preceding release's importer metadata after new assets
            # have been integrated into the authoritative texture manifest.
            stale = json.loads((root/'verification-android-import.json').read_text(encoding='utf-8'))
            stale.update(matching_texture_entries=1,pack_fingerprint='stale',current_payload_device_tested=True)
            (root/'verification-android-import.json').write_text(json.dumps(stale),encoding='utf-8')
            with patch.object(bump_version,'ROOT',root), redirect_stdout(StringIO()):
                bump_version.main(date(2026,11,7))
            updated = json.loads((root/'verification.json').read_text(encoding='utf-8'))
            imported = json.loads((root/'verification-android-import.json').read_text(encoding='utf-8'))
            self.assertEqual(updated['version'],imported['version'])
            self.assertEqual(manifest['pngs'],imported['matching_texture_entries'])
            self.assertEqual(manifest['pack_fingerprint'],imported['pack_fingerprint'])
            self.assertEqual(manifest['editions'],imported['editions'])
            self.assertEqual(manifest['android']['current_payload_device_tested'],imported['current_payload_device_tested'])
            self.assertIn('Same fonts, plus future reviewed menu artwork', (root/'README.md').read_text(encoding='utf-8'))


if __name__=='__main__':
    unittest.main()
