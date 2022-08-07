from unittest import TestCase
from data_access import *


class DataAccessTests(TestCase):
    def test_fetch_valid(self):
        data = fetch_by_id('001')
        self.assertEqual('001', data['id'])
        self.assertLessEqual(len(data), 4)
        self.assertGreaterEqual(len(data), 3)

    def test_fetch_invalid(self):
        data = fetch_by_id('999')
        self.assertIsNone(data)


if __name__ == '__main__':
    unittest.main()
