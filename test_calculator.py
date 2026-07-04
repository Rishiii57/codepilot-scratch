import unittest

# Assuming calculate_score is defined in a 'calculator' module
# For example, if calculate_score is in 'calculator.py', you would import it like this:
from calculator import calculate_score

class TestCalculator(unittest.TestCase):

    def test_calculate_score_with_zero_input(self):
        """
        Test that calculate_score(0) correctly returns 0,
        addressing the ZeroDivisionError bug.
        """
        result = calculate_score(0)
        self.assertEqual(result, 0, "Expected calculate_score(0) to return 0")

if __name__ == '__main__':
    unittest.main()
