import math
import time

import exceptions




# Defining Function
def writeToFile(name,text):
    file = open(name,"w")
    file.write(text)
    file.close()

def bisection(lower_bound, upper_bound, error_tolerance, bisection_function,max_step):
    if bisection_function(lower_bound) * bisection_function(upper_bound) > 0.0:
        text = ('Given guess values do not bracket the root.\n')
        text+= ('Try Again with different guess values.\n')
        raise exceptions.noRootInInterval(text)
    step = 1
    text = ('*** BISECTION METHOD IMPLEMENTATION ***\n')
    condition = True
    reached_max = False
    text+=('Iteration \t x2 \t    f(x2)\n')
    while condition:
        middle = (lower_bound + upper_bound) / 2
        text+=('%d         \t %0.6f\t %0.6f\n' % (step, middle, bisection_function(middle)))

        if bisection_function(lower_bound) * bisection_function(middle) < 0:
            upper_bound = middle
        else:
            lower_bound = middle

        if(step > max_step):
            reached_max = True
            raise exceptions.noRootInInterval('Cannot find a root in interval.\n')
            break

        step = step + 1
        condition = abs(bisection_function(middle)) > error_tolerance

    text += ('\nRequired Root is : %0.8f\n' % middle)
    writeToFile("bisectionOut.txt",text=text)
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

# Implementing Fixed Point Iteration Method
def fixed_point_iteration(initial_guess_fixed_point, error_tolerance, maximum_step,fixed_point_rewritten_function):
    print('\n\n*** FIXED POINT ITERATION ***')

    
    step = 1
    flag = 1
    condition = True
    oldx = initial_guess_fixed_point
    differrence = error_tolerance + 1 #garbage value to be deined
    while condition:
        new_value_fixed_point = fixed_point_rewritten_function(oldx)
        olddiff = differrence
        differrence = abs(new_value_fixed_point - oldx)
        print('Iteration:%d, x1 = %0.6f, difference= %0.6f' % (step, new_value_fixed_point,differrence))

        step = step + 1

        if step > maximum_step or olddiff<differrence:
            flag = 0
            break

        condition = differrence > error_tolerance
        oldx = new_value_fixed_point

    if flag == 1:
        print('\nRequired root is: %0.8f' % new_value_fixed_point)
        return new_value_fixed_point
    else:
        print('\nNot Convergent.')
        raise exceptions.notConvergent("Not convergent!")


def newton_raphson(initial_guess_newton_raphson, error_tolerance, maximum_step,newton_raphson_function,newton_raphson_rewritten_function):
    print('\n\n*** NEWTON RAPHSON METHOD IMPLEMENTATION ***')
    step = 1
    flag = 1
    condition = True
    while condition:
        if newton_raphson_rewritten_function(initial_guess_newton_raphson) == 0.0:
            print('Divide by zero error!')
            raise ValueError('Divide by zero error!')
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
        return new_value_newton_raphson
    else:
        print('\nNot Convergent.')
        raise exceptions.notConvergent("Not convergent!")
        
def secant(xi, ximinus1, error_tolerance, maximum_step,secant_function):
    print('\n\n*** SECANT METHOD IMPLEMENTATION ***')
    step = 1
    condition = True
    while condition:
        if secant_function(xi) == secant_function(ximinus1):
            print('Divide by zero error!')
            raise ValueError('Divide by zero error!')
            break

        xiplus1 = xi - (ximinus1 - xi) * secant_function(xi) / (secant_function(ximinus1) - secant_function(xi))
        print('Iteration-%d, x2 = %0.6f and f(x2) = %0.6f' % (step, xiplus1, secant_function(xiplus1)))
        xi = ximinus1
        ximinus1 = xiplus1
        step = step + 1

        if step > maximum_step:
            print('Not Convergent!')
            raise exceptions.notConvergent("Not convergent!")
            break

        condition = abs(secant_function(xiplus1)) > error_tolerance
    print('\n Required root is: %0.8f' % xiplus1)
    return xiplus1
