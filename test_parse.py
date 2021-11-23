import unittest
import parse
import math
import exceptions
import os
class TestParse(unittest.TestCase):
    def testGet_expression(self):
        expression = 'x**2 -6'
        x,expresion_parsed = parse.get_expression(expression)
        self.assertEqual(expresion_parsed.subs(x,2),-2)

        expression = 'sin x'
        with self.assertRaises(exceptions.badExpression):
            x,expresion_parsed = parse.get_expression(expression)

        expression = 'E**-x *(3.2 *sin(x)-0.5* cos(x))'
        x,expresion_parsed = parse.get_expression(expression)
        self.assertAlmostEqual(float(expresion_parsed.subs(x,2)),0.4219517,5)




    def testCall_bisection(self):
        lower_bound = 1
        upper_bound = 99
        expression = 'sin(x)'
        error_tolerance = 0.00001
        max_step = 100
        root =  parse.call_bisection(lower_bound,upper_bound,expression,error_tolerance,max_step)
        self.assertTrue(abs(math.sin(root))<error_tolerance)

       
        expression = ('sin x')
        with self.assertRaises(exceptions.badExpression):
            root =  parse.call_bisection(lower_bound,upper_bound,expression,error_tolerance,max_step)

        expression ='x^2 +3'
        with self.assertRaises(exceptions.noRootInInterval):
            root =  parse.call_bisection(lower_bound,upper_bound,expression,error_tolerance,max_step)

        if os.path.exists("bisectionOut.txt"):
             os.remove("bisectionOut.txt") 


    def testCall_false_position(self):
        f = lambda x:math.e**-x *(3.2*math.sin(x) - 0.5 * math.cos(x))
        expression = 'E**-x *(3.2 *sin(x)-0.5* cos(x))'
        lower_bound = 3
        upper_bound = 4
        error_tolerance = 0.001
        root = parse.call_false_position(lower_bound,upper_bound,expression,error_tolerance)
        self.assertAlmostEqual(f(root),0,2)

    def testCall_newton_raphson(self):
        initial_guess = 0.05
        error_tolerance = 0.0001
        max_step = 5
        expression = 'x**3 - 0.165*(x**2) + 3.993*10**-4'
        f = lambda x: x**3 - 0.165*(x**2) + 3.993e-4
        root = parse.call_newton_raphson(initial_guess,expression,error_tolerance,max_step)
        self.assertLess(abs(f(root)),error_tolerance)

        differentiation = "3*x**2 - 0.33*x"
        root = parse.call_newton_raphson(initial_guess,differentiation,expression,error_tolerance,max_step)
        self.assertLess(abs(f(root)),error_tolerance)
    
    def testCall_fixed_point(self):
        initial_guess = 0
        error_tolerance = 0.5*10**-3
        max_step = 20
        expression = 'E**-x'

        root = parse.call_fixed_point(initial_guess,expression,error_tolerance,max_step)
        self.assertAlmostEqual(root,0.567,3)

    def testCall_Secant(self):
        xi = 1
        ximinus1 = 0
        error_tolerance = 0.5*10**-3
        max_step = 4
        f= 'E^-x -x'
        root = parse.call_secant(ximinus1,xi,f,error_tolerance,max_step)
        self.assertAlmostEqual(root,0.567,3)

    def testFileToDict(self):
        testData = {
            'method':'bisection',
                'lower bound':1,
                'upper bound':2,
                'expression':'x^2-3'
            
        }
        data = parse.fileToDict("testData.json")
        self.assertEqual(data,testData)

    def testCall_from_dict(self):
        testData = {
            'method':'bisection',
                'lower bound':1,
                'upper bound':2,
                'expression':'x^2-3'
        }
        root = parse.call_from_dict(testData)
        if os.path.exists("bisectionOut.txt"):
             os.remove("bisectionOut.txt") 
        self.assertAlmostEqual(root,math.sqrt(3),4)

if __name__ == '__main__':
    unittest.main()