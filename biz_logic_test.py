import unittest
import biz_logic


class BizLogicTest(unittest.TestCase):
    def test_no_discount_zero_items(self):
        self.assertEqual(0, biz_logic.calc_price(0, 100))

    def test_no_discount_one_items(self):
        self.assertEqual(100, biz_logic.calc_price(1, 100))

    def test_no_discount_n_items(self):
        self.assertEqual(600, biz_logic.calc_price(6, 100))

    def test_discount_zero_items(self):
        self.assertEqual(0, biz_logic.calc_price(0, 100, 3, 200))

    def test_discount_not_enough_items(self):
        self.assertEqual(600, biz_logic.calc_price(2, 300, 3, 500))

    def test_discount_just_enough_items(self):
        self.assertEqual(500, biz_logic.calc_price(3, 300, 3, 500))

    def test_discount_to_many_items(self):
        self.assertEqual(800, biz_logic.calc_price(4, 300, 3, 500))

    def test_discount_double_items(self):
        self.assertEqual(1000, biz_logic.calc_price(6, 300, 3, 500))

    def test_discount_double_plus_items(self):
        self.assertEqual(1600, biz_logic.calc_price(8, 300, 3, 500))


if __name__ == '__main__':
    unittest.main()
