import unittest

from store import apply_discount, can_checkout, loyalty_discount, shipping_cost


class StoreTests(unittest.TestCase):
    def test_regular_shipping(self):
        self.assertEqual(shipping_cost(500), 99.0)

    def test_negative_subtotal_is_invalid(self):
        with self.assertRaises(ValueError):
            shipping_cost(-1)

    def test_apply_discount(self):
        self.assertEqual(apply_discount(1000, 10), 900.0)

    # Test cases for apply discount, percentage should be between 0 and 100
    def test_apply_discount_with_negative_discount(self):
        with self.assertRaises(ValueError):
            apply_discount(1000, -10)

    def test_apply_discount_with_zero_discount(self):
        self.assertEqual(apply_discount(1000, 0), 1000.0)

    def test_apply_discount_with_discount_over_100(self):
        with self.assertRaises(ValueError):
            apply_discount(1000, 110)

    def test_apply_discount_with_discount_equal_100(self):
        self.assertEqual(apply_discount(1000, 100), 0.0)

    def test_checkout_with_items(self):
        self.assertTrue(can_checkout(1))

    def test_loyalty_starts_at_zero(self):
        self.assertEqual(loyalty_discount(0), 0)


if __name__ == "__main__":
    unittest.main()
