import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ContractTests(unittest.TestCase):
    def test_source(self):
        source = json.loads((ROOT / 'sources.json').read_text())
        self.assertEqual(len(source['sha']), 40)
        self.assertEqual(source['release'], 'v1.2.5')

    def test_no_second_gateway_or_ports(self):
        compose = (ROOT / 'compose.yml').read_text()
        self.assertNotIn('ports:', compose)
        self.assertNotIn('build:', compose)
        self.assertIn('deploy_sub2api-network', compose)
        self.assertIn('GHProxy requires verified digest', compose)

    def test_restrict_routes(self):
        caddy = (ROOT / 'config/Caddyfile.fragment').read_text()
        self.assertIn('git-upload-pack', caddy)
        self.assertNotIn('git-receive-pack', caddy)
        self.assertIn('remote_ip 115.190.243.21', caddy)
        self.assertIn('respond 403', caddy)
        self.assertIn('header_up -Authorization', caddy)


if __name__ == '__main__':
    unittest.main()
