import unittest
import main
import math


class TestMain(unittest.TestCase):

    def testBisection(self):
        lower_bound = 1
        upper_bound = 99
        function = lambda x : math.sin(x)
        error_tolerance = 0.00001
        max_step = 100

        root = main.bisection(lower_bound,upper_bound,error_tolerance,function,max_step)

        self.assertTrue(abs(function(root))<error_tolerance)

        f = lambda x: x**2
        lower_bound = -10
        upper_bound = 0
        error_tolerance = 0.000001
        max_step =  10
        with self.assertRaises(Exception):
            root2 = main.bisection(lower_bound,upper_bound,error_tolerance,f,max_step)


    def testFalse_position(self):
        lower_bound = 3
        upper_bound = 4
        error_tolerance = 0.001
        f = lambda x : math.e**-x *(3.2*math.sin(x) - 0.5 * math.cos(x))

        root = main.false_position(lower_bound,upper_bound,error_tolerance,f)
        self.assertTrue(abs(f(root))<error_tolerance)

    def testFixed_point_iteration(self):
        initial_guess = 0
        error_tolerance = 0.001
        max_step = 15

        f = lambda x:math.e**-x - x
        g = lambda x:math.e**-x

        root = main.fixed_point_iteration(initial_guess,error_tolerance,max_step,f,g)
        self.assertTrue(abs(f(root))<error_tolerance)

        initial_guess = 4
        error_tolerance = 0.01
        max_step = 100

        f = lambda x:x**2 -2*x -3
        g1 = lambda x:math.sqrt(2*x+3)
        g2 = lambda x:(x**2 -3)/2

        root1 = main.fixed_point_iteration(initial_guess,error_tolerance,max_step,f,g1)
        self.assertTrue(abs(f(root1))<error_tolerance)

        with self.assertRaises(Exception):
            root2 = main.fixed_point_iteration(initial_guess,error_tolerance,max_step,f,g2)


    def testNewton_raphson(self):
        initial_guess = 0.05
        error_tolerance = 0.0001
        max_step = 5
        f = lambda x: x**3 - 0.165*(x**2) + 3.993e-4
        g = lambda x: 3*x**2 - 0.33*x
        root = main.newton_raphson(initial_guess,error_tolerance,max_step,f,g)
        self.assertTrue(abs(f(root))<error_tolerance)

        initial_guess = 0.11
        with self.assertRaises(ValueError):
            root2 = main.newton_raphson(initial_guess,error_tolerance,max_step,f,g)

    def testSecant(self):
        xi = 1
        ximinus1 = 0
        error_tolerance = 0.0001
        max_step = 4
        f= lambda x: math.e**-x -x
        root = main.secant(xi,ximinus1,error_tolerance,max_step,f)
        self.assertTrue(abs(f(root))<error_tolerance)



if __name__ == '__main__':
    unittest.main()