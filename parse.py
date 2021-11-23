from sympy import *
from exceptions import *
import main
from multipledispatch import dispatch
import json

#some rules when passing strings:
# e has to be capital E
# multiplication has to be x*y and not xy , same in 2*x not 2x etc...

#TODO: read from JSON file
#TODO: method to call a given method
#TODO: output to file

def get_expression(expression):
    x = Symbol('x')
    try:
        expression_parsed = sympify(expression,convert_xor=True)
    except :
        raise badExpression('Expression cannot be solved.')
    else:
        return x , expression_parsed

def call_bisection(lower_bound,upper_bound,expression,error_tolerance=0.00001,max_step=50):
    x , expression_parsed = get_expression(expression)
    f = lambda y:float( expression_parsed.subs(x,y))
    return main.bisection(lower_bound,upper_bound,error_tolerance,f,max_step)


def call_false_position(lower_bound,upper_bound,expression,error_tolerance=0.00001):
    x,expression_parsed = get_expression(expression)
    f = lambda y: float(expression_parsed.subs(x,y))
    return main.false_position(lower_bound,upper_bound,error_tolerance,f)

@dispatch(float,str,float,int)
def call_newton_raphson(initial_guess,expression,error_tolerance=0.00001,max_step=50):
    x ,  expression_parsed = get_expression(expression)
    f = lambda y : float(expression_parsed.subs(x,y))
    try:
        f_dash = diff(expression_parsed,x)
        g = lambda y : float(f_dash.subs(x,y))
    except:
        raise cannotDiffererntiate('Cannot find a differentaition for this expression.\n')
    
    return main.newton_raphson(initial_guess,error_tolerance,max_step,f,g)

@dispatch(float,str,str,float,int)
def call_newton_raphson(initial_guess,differentiation,expression,error_tolerance=0.00001,max_step=50):
    x ,  expression_parsed = get_expression(expression)
    f = lambda y : float(expression_parsed.subs(x,y))
    x , differentiation_parsed = get_expression(differentiation)
    g = lambda y : float(differentiation_parsed.subs(x,y))
    return main.newton_raphson(initial_guess,error_tolerance,max_step,f,g)

def call_fixed_point(initial_guess,expression,error_tolerance=0.00001,max_step=50):
    x, expression_parsed = get_expression(expression)
    g = lambda y: float(expression_parsed.subs(x,y))
    return(main.fixed_point_iteration(initial_guess,error_tolerance,max_step,g))

def call_secant(guess1,guess2,expression,error_tolerance=0.00001,max_step=50):
    x, expression_parsed = get_expression(expression)
    f = lambda y: float(expression_parsed.subs(x,y))
    return main.secant(guess2,guess1,error_tolerance,max_step,f)

def fileToDict(fileName = 'input.json'):
    f = open(fileName,'r')
    data = json.load(f)
    f.close()
    return data

def call_from_dict(data):
    method = data['method']
    if method == 'bisection':
        return call_bisection(
            lower_bound=data['lower bound'],
            upper_bound=data['upper bound'],
            expression=data['expression'],
            error_tolerance=data.get('error tolerance',0.00001),
            max_step=data.get('max step',50)
        )
    elif method == 'false position' or 'regula falsi':
        return call_false_position(
            lower_bound=data['lower bound'],
            upper_bound=data['upper bound'],
            expression=data['expression'],
            error_tolerance=data.get('error tolerance',0.00001),
            max_step=data.get('max step',50)            
        )