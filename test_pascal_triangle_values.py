import explore_pascals_triangle
import unittest

class TestProblem1(unittest.TestCase):
    knownValues = ( ((0, 0), 1), # (row, col), expected_value
                    ((1, 0), 1),
                    ((1, 1), 1),
                    ((2, 1), 2),
                    ((4, 2), 6),
                    ((10, 7), 120))

    def test_method_C_to_known_values(self):
        """C function should give known result with known input"""
        for location, pascal_value in self.knownValues:              
            result = explore_pascals_triangle.C(location[0], location[1])
            self.assertEqual(pascal_value, result)   

    def test_method_calc_pascal_value_to_known_values(self):
        """calc_pascal_value function should give known result with known input"""
        for location, pascal_value in self.knownValues:              
            result = explore_pascals_triangle.calc_pascal_value(location[0], location[1])
            self.assertEqual(pascal_value, result)   

if __name__ == '__main__':
    unittest.main()