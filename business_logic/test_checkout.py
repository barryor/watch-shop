# Tests for functionality in checkout.py

import unittest
from unittest import TestCase
from business_logic import checkout


class TestNoDiscountSingleWatch(TestCase):

    def setUp(self) -> None:
        self.test_data = {'id': '003', 'name': 'Swatch', 'unit_price': '50', 'discount': None}

    def test_zero_items(self):
        self.assertEqual(0, checkout.calc_watch_price(self.test_data, 0))

    def test_one_items(self):
        self.assertEqual(50, checkout.calc_watch_price(self.test_data, 1))

    def test_n_items(self):
        self.assertEqual(300, checkout.calc_watch_price(self.test_data, 6))


class TestWithDiscountSingleWatch(TestCase):
    def setUp(self) -> None:
        self.test_data = {'id': '002', 'name': 'Michael Kors',
                          'unit_price': '80', 'discount': '2 for 120'}

    def test_zero_items(self):
        self.assertEqual(0, checkout.calc_watch_price(self.test_data, 0))

    def test_not_enough_items(self):
        self.assertEqual(80, checkout.calc_watch_price(self.test_data, 1))

    def test_just_enough_items(self):
        self.assertEqual(120, checkout.calc_watch_price(self.test_data, 2))

    def test_to_many_items(self):
        self.assertEqual(200, checkout.calc_watch_price(self.test_data, 3))

    def test_double_items(self):
        self.assertEqual(240, checkout.calc_watch_price(self.test_data, 4))

    def test_discount_double_plus_items(self):
        self.assertEqual(320, checkout.calc_watch_price(self.test_data, 5))


# NOTE: These tests run with the live data_layer access dependency in place.
# TODO: Mock this here and move these to a separate sub integration test file
class TestFullCalculation(TestCase):
    def test_zero_items(self):
        self.assertEqual(0, checkout.calculate_total([]))

    def test_one_items(self):
        self.assertEqual(80, checkout.calculate_total(['002']))

    def test_one_of_each(self):
        self.assertEqual(260, checkout.calculate_total(['001', '002', '003', '004']))

    def test_discounted_items(self):
        self.assertEqual(320, checkout.calculate_total(['001', '001', '001', '002', '002']))

    def test_invalid_request(self):
        self.assertIsNone(checkout.calculate_total(['999']))

    def test_no_data(self):
        self.assertIsNone(checkout.calculate_total(None))

    def test_too_many_items(self):
        big_list = ['001' for n in range(0, checkout.MAX_ORDER_SIZE + 1)]
        self.assertIsNone(checkout.calculate_total(big_list))


if __name__ == '__main__':
    unittest.main()
