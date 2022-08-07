import unittest
from unittest import TestCase
from biz_logic import calc_watch_price  # testing inside the module
from biz_logic import calculate_total  # Testing the interface


class TestNoDiscountSingleWatch(TestCase):

    def setUp(self) -> None:
        self.test_data = {'id': '003', 'name': 'Swatch', 'unit_price': '50', 'discount': None}

    def test_zero_items(self):
        self.assertEqual(0, calc_watch_price(self.test_data, 0))

    def test_one_items(self):
        self.assertEqual(50, calc_watch_price(self.test_data, 1))

    def test_n_items(self):
        self.assertEqual(300, calc_watch_price(self.test_data, 6))


class TestWithDiscountSingleWatch(TestCase):
    def setUp(self) -> None:
        self.test_data = {'id': '002', 'name': 'Michael Kors',
                          'unit_price': '80', 'discount': '2 for 120'}

    def test_zero_items(self):
        self.assertEqual(0, calc_watch_price(self.test_data, 0))

    def test_not_enough_items(self):
        self.assertEqual(80, calc_watch_price(self.test_data, 1))

    def test_just_enough_items(self):
        self.assertEqual(120, calc_watch_price(self.test_data, 2))

    def test_to_many_items(self):
        self.assertEqual(200, calc_watch_price(self.test_data, 3))

    def test_double_items(self):
        self.assertEqual(240, calc_watch_price(self.test_data, 4))

    def test_discount_double_plus_items(self):
        self.assertEqual(320, calc_watch_price(self.test_data, 5))


# NOTE: These tests run with the live data access dependency in place.
# TODO: Mock this here and move these to a separate sub integration test file
class TestFullCalculation(TestCase):
    def test_zero_items(self):
        self.assertEqual(0, calculate_total([]))

    def test_one_items(self):
        self.assertEqual(80, calculate_total(['002']))

    def test_one_of_each(self):
        self.assertEqual(260, calculate_total(['001', '002', '003', '004']))

    def test_discounted_items(self):
        self.assertEqual(320, calculate_total(['001', '001', '001', '002', '002']))


if __name__ == '__main__':
    unittest.main()
