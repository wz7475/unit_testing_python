import unittest
import calculator


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(2, 6), 8)
        self.assertEqual(calculator.add(-2, 6), 4)
        self.assertEqual(calculator.add(-2, -6), -8)

    def test_divide(self):
        self.assertEqual(calculator.divide(10, 5), 2)
        self.assertEqual(calculator.divide(5, 2), 2.5)

        with self.assertRaises(ZeroDivisionError):
            calculator.divide(10,0)


if __name__ == '__main__':
    unittest.main()
