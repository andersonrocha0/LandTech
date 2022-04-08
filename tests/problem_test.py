import unittest

from src.problem import get_land_parcels_for_company


class MyTestCase(unittest.TestCase):
    def test_problem(self):
        result = get_land_parcels_for_company("c1")

        # l1, l3, l4, l5

        self.assertEqual({"l1", "l3", "l4", "l5"}, result)  # add assertion here


if __name__ == '__main__':
    unittest.main()
