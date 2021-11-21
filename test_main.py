import unittest
import main
import math


class TestMain(unittest.TestCase):

    def testBisection(self):
        lower_bound = 1
        upper_bound = 99
        function = lambda x : math.sin(x)
        error_tolerance = 0.00001

        root = main.bisection(lower_bound,upper_bound,error_tolerance,function)

        self.assertTrue(abs(function(root))<error_tolerance)

    def testFalse_position(self):
        lower_bound = 3
        upper_bound = 4
        error_tolerance = 0.001
        f = lambda x : math.e**-x *(3.2*math.sin(x) - 0.5 * math.cos(x))

        root = main.false_position(lower_bound,upper_bound,error_tolerance,f)
        self.assertTrue(abs(f(root))<error_tolerance)



if __name__ == '__main__':
    unittest.main()