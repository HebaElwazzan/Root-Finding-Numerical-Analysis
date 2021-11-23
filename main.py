import time
import json

import exceptions

# Defining Function
def writeToJSONFile(data,name='out/out.json'):
    file = open(name,'w')
    json.dump(data,file)
    file.close()

def bisection(lower_bound, upper_bound, error_tolerance, bisection_function,max_step,fileName='out/bisectionOut.json'):
    if bisection_function(lower_bound) * bisection_function(upper_bound) > 0.0:
        text = ('Given guess values do not bracket the root.\n')
        text+= ('Try Again with different guess values.\n')
        raise exceptions.noRootInInterval(text)
    step = 1
    data = {'method':'Bisection'}
    condition = True
    reached_max = False
    data['x2']=[]
    data['f(x2)']=[]
    data['iterations']=1
    while condition:
        middle = (lower_bound + upper_bound) / 2
        data['x2'].append(middle)
        data['f(x2)'].append(bisection_function(middle))
        if bisection_function(lower_bound) * bisection_function(middle) < 0:
            upper_bound = middle
        else:
            lower_bound = middle

        if(step > max_step):
            data['status']='bad'
            data['exception']='noRootInInterval'
            writeToJSONFile(data=data,name=fileName)
            raise exceptions.noRootInInterval('Cannot find a root in interval.\n')
            break
        
        data['iterations']+=1
        step = step + 1
        condition = abs(bisection_function(middle)) > error_tolerance

    data['root']=middle
    data['status']='good'

    writeToJSONFile(data=data,name=fileName)
    return middle


# Implementing False Position Method
def false_position(lower_bound, upper_bound, error_tolerance, false_position_function,fileName='out/falsePosOut.json'):
    data= {
        'method':'False Position'
    }
    if false_position_function(lower_bound) * false_position_function(upper_bound) > 0.0:
        data['status']='bad'
        data['exception']='noRootInInterval'
        writeToJSONFile(data=data,name=fileName)
        raise exceptions.noRootInInterval("Given guess values do not bracket the root.")
    step = 1
    data['iterations']=0
    data['x2']=[]
    data['f(x2)']=[]
    data['updates']=[]
    condition = True
    while condition:
        middle = lower_bound - (upper_bound-lower_bound) * false_position_function(lower_bound)/(false_position_function(upper_bound) - false_position_function(lower_bound))
        data['x2'].append(middle)
        data['f(x2)'].append(false_position_function(middle))
        if false_position_function(lower_bound) * false_position_function(middle) < 0:
            upper_bound = middle
            data['updates'].append('upper bound = x2')
        else:
            lower_bound = middle
            data['updates'].append('lower bound = x2')
        data['iterations']+=1
        step = step + 1
        condition = abs(false_position_function(middle)) > error_tolerance

    data['root']=middle
    data['status']='good'
    writeToJSONFile(data=data,name=fileName)
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
