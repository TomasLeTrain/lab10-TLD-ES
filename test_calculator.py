import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
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
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
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
