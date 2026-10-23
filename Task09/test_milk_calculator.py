import unittest
from decimal import Decimal
from milk_calculator import rate_per_litre, payout

class MilkCalculatorTests(unittest.TestCase):
    def test_standard_rate(self):
        self.assertEqual(rate_per_litre("3.5", "8.5"), Decimal("30.00"))
    def test_above_reference(self):
        self.assertEqual(rate_per_litre("4.2", "8.7"), Decimal("33.40"))
    def test_below_reference(self):
        self.assertEqual(rate_per_litre("3.1", "8.3"), Decimal("27.80"))
    def test_payment(self):
        self.assertEqual(payout("8.5", "4.2", "8.7"), Decimal("283.90"))
    def test_lowest_fat_boundary(self):
        self.assertEqual(payout("1", "2.0", "8.5"), Decimal("24.00"))
    def test_highest_fat_boundary(self):
        self.assertEqual(payout("1", "7.0", "8.5"), Decimal("44.00"))
    def test_negative_litres_rejected(self):
        with self.assertRaises(ValueError):
            payout("-1", "3.5", "8.5")
    def test_out_of_range_fat_rejected(self):
        with self.assertRaises(ValueError):
            payout("1", "7.1", "8.5")

if __name__ == "__main__":
    unittest.main()
