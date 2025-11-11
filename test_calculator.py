# https://github.com/TomasLeTrain/lab10-TLD-ES
# Partner 1: Tomas Lopez Devia
# Partner 2: Ethan Scheer

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-30, 3), -27)
        self.assertEqual(add(10000, 10000), 20000)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(30, 31), -1)
        self.assertEqual(subtract(-300, 3), -303)
        self.assertEqual(subtract(1000000, 1000000), 0)
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertAlmostEqual(mul(3,4), 12)
        self.assertAlmostEqual(mul(0,10), 0)
        self.assertAlmostEqual(mul(-1000,-67), 67000)


    def test_divide(self): # 3 assertions
        self.assertAlmostEqual(div(4,12), 3)
        self.assertAlmostEqual(div(10,0), 0)
        self.assertAlmostEqual(div(40,40), 1)
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0,100)

    def test_logarithm(self): # 3 assertions
        self.assertAlmostEqual(logarithm(2, 8), 3.0)
        self.assertAlmostEqual(logarithm(10, 10000), 4)
        self.assertAlmostEqual(logarithm(8, 64), 2)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(10, -10000)
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, -10)

    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(3,4), 5)
        self.assertAlmostEqual(hypotenuse(-5,12), 13)
        self.assertAlmostEqual(hypotenuse(8,15), 17)


    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
           square_root(-10)
        self.assertAlmostEqual(square_root(100), 10)
        self.assertAlmostEqual(square_root(0), 0)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()
