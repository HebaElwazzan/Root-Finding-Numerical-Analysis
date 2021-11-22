import unittest
import parse
import math

class TestParse(unittest.TestCase):
    def testCall_bisection(self):
        lower_bound = 1
        upper_bound = 99
        expression = 'sin(x)'
        error_tolerance = 0.00001
        max_step = 100
        root =  parse.call_bisection(lower_bound,upper_bound,error_tolerance,expression,max_step)
        self.assertTrue(abs(math.sin(root))<error_tolerance)


if __name__ == '__main__':
    unittest.main()