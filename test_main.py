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

        self.assertTrue(abs(root - 40.8407045)<error_tolerance)

    def testFalsePosition(self):
        lower_bound = 3
        upper_bound = 4
        error_tolerance = 0.001
        f = lambda x : math.e**-x *(3.2*math.sin(x) - 0.5 * math.cos(x))

        root = main.falsePosition(lower_bound,upper_bound,error_tolerance,f)
        self.assertTrue(abs(root - 3.296589396))



if __name__ == '__main__':
    unittest.main()