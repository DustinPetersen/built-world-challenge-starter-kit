from pathlib import Path
import sys
from urllib.parse import parse_qs,urlsplit
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'examples'))
from edmonton_permits import query_url,normalize

class EdmontonTests(unittest.TestCase):
    def test_date_window_and_aggregate_only(self):
        url=query_url(2025)
        self.assertEqual(urlsplit(url).netloc,'data.edmonton.ca')
        query=parse_qs(urlsplit(url).query)
        self.assertEqual(query['$select'],['building_type,count(*) as permit_rows'])
        self.assertIn("issue_date >= '2025-01-01T00:00:00'",query['$where'][0])
        self.assertIn("issue_date < '2026-01-01T00:00:00'",query['$where'][0])
        self.assertEqual(query['$limit'],['100'])
    def test_unknown_classification_is_preserved(self):
        self.assertEqual(normalize([{'permit_rows':'4'}]),[{'building_type':'(unclassified)','permit_rows':4}])
    def test_reject_invalid_year(self):
        for year in [True,'2025',2008,2101]:
            with self.assertRaises(ValueError):query_url(year)
    def test_reject_negative_upstream_count(self):
        with self.assertRaises(ValueError):normalize([{'permit_rows':'-1'}])

if __name__=='__main__': unittest.main()
