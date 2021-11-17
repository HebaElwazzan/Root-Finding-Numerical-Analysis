from sympy import *

x = Symbol('x')

#suppose the user input is converted to a string
expr = sympify("x**2+3*x+4")
print(diff(expr));

def f(y):
    return(expr.subs(x,y));

print(f(5))
