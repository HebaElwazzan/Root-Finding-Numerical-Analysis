from sympy import *
import main

#a set of functions that act as drivers or adapters between gui and algorithms
x = Symbol('x')

#suppose the user input is converted to a string
expr = sympify("x**2+3*x+4")

print(diff(expr));

def f(y):
    return(expr.subs(x,y));

print(f(5))

def call_bisection(lower_bound,upper_bound,error_tolerance,expression,max_step):
    x = Symbol('x')
    expression_parsed = sympify(expression)
    f = lambda y: expression_parsed.subs(x,y)
    return main.bisection(lower_bound,upper_bound,error_tolerance,f,max_step)

