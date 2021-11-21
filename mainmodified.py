import math
import time
# Defining Function


'''def bisection_function(x):
    return x**3-5*x-9'''


def bisection(lower_bound, upper_bound, error_tolerance, bisection_function):
    if bisection_function(lower_bound) * bisection_function(upper_bound) > 0.0:
        print('Given guess values do not bracket the root.')
        print('Try Again with different guess values.')
    step = 1
    print('\n\n*** BISECTION METHOD IMPLEMENTATION ***')
    condition = True
    while condition:
        middle = (lower_bound + upper_bound) / 2
        print('Iteration-%d, x2 = %0.6f and f(x2) = %0.6f' % (step, middle, bisection_function(middle)))

        if bisection_function(lower_bound) * bisection_function(middle) < 0:
            upper_bound = middle
        else:
            lower_bound = middle

        step = step + 1
        condition = abs(bisection_function(middle)) > error_tolerance

    print('\nRequired Root is : %0.8f' % middle)
    return middle


# Implementing False Position Method
def false_position(lower_bound, upper_bound, error_tolerance, false_position_function):
    if false_position_function(lower_bound) * false_position_function(upper_bound) > 0.0:
        print('Given guess values do not bracket the root.')
        print('Try Again with different guess values.')
    step = 1
    print('\n\n*** FALSE POSITION METHOD IMPLEMENTATION ***')
    condition = True
    while condition:
        middle = lower_bound - (upper_bound-lower_bound) * false_position_function(lower_bound)/(false_position_function(upper_bound) - false_position_function(lower_bound))
        print('Iteration-%d, x2 = %0.6f and f(x2) = %0.6f' % (step, middle, false_position_function(middle)))

        if false_position_function(lower_bound) * false_position_function(middle) < 0:
            upper_bound = middle
        else:
            lower_bound = middle

        step = step + 1
        condition = abs(false_position_function(middle)) > error_tolerance

    print('\nRequired root is: %0.8f' % middle)
    return middle


def fixed_position_function(x):
    return x*x*x + x*x - 1


# Re-writing f(x)=0 to x = g(x)
def fixed_position_rewritten_function(x):
    return 1/math.sqrt(1+x)


# Implementing Fixed Point Iteration Method
def fixed_point_iteration(initial_guess_fixed_position, error_tolerance, maximum_step):
    print('\n\n*** FIXED POINT ITERATION ***')
    step = 1
    flag = 1
    condition = True
    while condition:
        new_value_fixed_position = fixed_position_rewritten_function(initial_guess_fixed_position)
        print('Iteration-%d, x1 = %0.6f and f(x1) = %0.6f' % (step, new_value_fixed_position, fixed_position_function(new_value_fixed_position)))
        initial_guess_fixed_position = new_value_fixed_position

        step = step + 1

        if step > maximum_step:
            flag = 0
            break

        condition = abs(fixed_position_function(new_value_fixed_position)) > error_tolerance

    if flag == 1:
        print('\nRequired root is: %0.8f' % new_value_fixed_position)
    else:
        print('\nNot Convergent.')


def newton_raphson_function(x):
    return x*x*x + x*x - 1


# Re-writing f(x)=0 to x = g(x)
def newton_raphson_rewritten_function(x):
    return 1/math.sqrt(1+x)


def newton_raphson(initial_guess_newton_raphson, error_tolerance, maximum_step):
    print('\n\n*** NEWTON RAPHSON METHOD IMPLEMENTATION ***')
    step = 1
    flag = 1
    condition = True
    while condition:
        if newton_raphson_rewritten_function(initial_guess_newton_raphson) == 0.0:
            print('Divide by zero error!')
            break

        new_value_newton_raphson = initial_guess_newton_raphson - newton_raphson_function(initial_guess_newton_raphson) / newton_raphson_rewritten_function(initial_guess_newton_raphson)
        print('Iteration-%d, x1 = %0.6f and f(x1) = %0.6f' % (step, new_value_newton_raphson, newton_raphson_function(new_value_newton_raphson)))
        initial_guess_newton_raphson = new_value_newton_raphson
        step = step + 1

        if step > maximum_step:
            flag = 0
            break

        condition = abs(newton_raphson_function(new_value_newton_raphson)) > error_tolerance

    if flag == 1:
        print('\nRequired root is: %0.8f' % new_value_newton_raphson)
    else:
        print('\nNot Convergent.')


# Implementing Secant Method
def secant_function(x):
    return x**3 - 5*x - 9


def secant(xi, ximinus1, error_tolerance, maximum_step):
    print('\n\n*** SECANT METHOD IMPLEMENTATION ***')
    step = 1
    condition = True
    while condition:
        if secant_function(xi) == secant_function(ximinus1):
            print('Divide by zero error!')
            break

        xiplus1 = xi - (ximinus1 - xi) * secant_function(xi) / (secant_function(ximinus1) - secant_function(xi))
        print('Iteration-%d, x2 = %0.6f and f(x2) = %0.6f' % (step, xiplus1, secant_function(xiplus1)))
        xi = ximinus1
        ximinus1 = xiplus1
        step = step + 1

        if step > maximum_step:
            print('Not Convergent!')
            break

        condition = abs(secant_function(xiplus1)) > error_tolerance
    print('\n Required root is: %0.8f' % xiplus1)


def main():
    # Input Section
    '''
    xs = input('Enter First Guess for secant: ')
    xm = input('Enter Second Guess for secant: ')
    e1 = input('Tolerable Error for secant: ')
    N1 = input('Maximum Step for secant: ')

    # Converting lower_bound and e to float
    xs = float(xs)
    xm = float(xm)
    e1 = float(e1)

    # Converting N to integer
    N1 = int(N1)'''



    # Checking Correctness of initial guess values and false positioning

'''
    startfalse= time.time();
    falsePosition(lower_bound,upper_bound,error_tolerance)
    print("time for false position is " ,time.time()-startfalse);
    startbi = time.time();
    bisection(lower_bound,upper_bound,error_tolerance)
    print("time for bisection is ", time.time() - startbi);
    startfixed = time.time();
    fixedPointIteration(X, E, N)
    print("time for fixed is ", time.time() - startfixed);
    startnewton = time.time();
    newtonRaphson(X, E, N)
    print("time for newton raphson is ", time.time() - startnewton);

    startsecant=time.time();
    secant(xs,xm,e1,N1)
    print("time for secant is ", time.time() - startsecant);'''