import time
import json
import os
import exceptions
import re

# Util
def writeToJSONFile(data,name='out/out.json'):
    file = open(name,'w')
    json.dump(data,file)
    file.close()

#util
def createOutputFolder(name='out'):
    try:
        os.mkdir(name)
    except FileExistsError:
        pass

def bisection(lower_bound, upper_bound, error_tolerance, bisection_function,max_step,fileName='out/bisectionOut.json'):
    createOutputFolder()
    if bisection_function(lower_bound) * bisection_function(upper_bound) > 0.0:
        text = ('Given guess values do not bracket the root.\n')
        text+= ('Try Again with different guess values.\n')
        raise exceptions.noRootInInterval(text)
    step = 1
    data = {'method':'Bisection'}
    condition = True
    data['x2']=[]
    data['f(x2)']=[]
    data['iterations']=1
    data['updates']=[]
    start = time.perf_counter() *1000
    middle=lower_bound
    while condition:
        oldMiddle=middle
        middle = (lower_bound + upper_bound) / 2
        data['x2'].append(middle)
        data['f(x2)'].append(bisection_function(middle))
        if bisection_function(lower_bound) * bisection_function(middle) < 0:
            upper_bound = middle
            data['updates'].append('upper bound = x')
        else:
            lower_bound = middle
            data['updates'].append('lower bound = x')

        if(step > max_step):
            data['status']='bad'
            data['exception']='noRootInInterval'
            writeToJSONFile(data=data,name=fileName)
            raise exceptions.noRootInInterval('Cannot find a root in interval.\n')
            break
        
        data['iterations']+=1
        step = step + 1
        condition = abs(bisection_function(middle)) > error_tolerance
    duration = time.perf_counter()*1000 - start
    data['root']=middle
    data['status']='good'
    data['precision percentage']=100- (abs(1-(middle/oldMiddle))*100)
    data['time']=duration #in milliseconds
    writeToJSONFile(data=data,name=fileName)
    return middle


# Implementing False Position Method
def false_position(lower_bound, upper_bound, error_tolerance, false_position_function,max_step,fileName='out/falsePosOut.json'):
    createOutputFolder()
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
    data['xl']=[]
    data['xu']=[]
    data['f(xl)']=[]
    data['f(xu)']=[]
    data['updates']=[]
    data['x`']=[]
    data['f(x`)'] = []
    condition = True
    start = time.perf_counter()*1000
    oldx=lower_bound
    while condition:
        middle = lower_bound - (upper_bound-lower_bound) * false_position_function(lower_bound)/(false_position_function(upper_bound) - false_position_function(lower_bound))
        data['xl'].append(lower_bound)
        data['f(xl)'].append(false_position_function(lower_bound))
        data['xu'].append(upper_bound)
        data['f(xu)'].append(false_position_function(upper_bound))
        data['x`'].append(middle)
        data['f(x`)'].append(false_position_function(middle))
        if data['f(xl)'] * data['f(x`'] < 0:
            upper_bound = middle
            data['updates'].append('xu = x`')
        else:
            lower_bound = middle
            data['updates'].append('xl = x`')
        data['iterations']+=1
        step = step + 1
        condition = abs(false_position_function(middle)) > error_tolerance and step<=max_step
        precision = 100-abs(1-(middle/oldx))
        oldx=middle
    data['time']= time.perf_counter()*1000 - start
    data['root']=middle
    data['status']='good'
    data['precision percentage']=precision
    writeToJSONFile(data=data,name=fileName)
    return middle

# Implementing Fixed Point Iteration Method
def fixed_point_iteration(initial_guess_fixed_point, error_tolerance, maximum_step,fixed_point_rewritten_function,fileName='out/fixedPointOut.json'):
    createOutputFolder
    data={'method':'fixed point'}    
    step = 1
    flag = 1
    condition = True
    oldx = initial_guess_fixed_point
    differrence = error_tolerance + 1 #garbage value to be deined
    data['iterations']=0
    data['x1']=[]
    data['difference']=[]
    start = time.perf_counter()*1000
    while condition:
        new_value_fixed_point = fixed_point_rewritten_function(oldx)
        olddiff = differrence
        differrence = abs(new_value_fixed_point - oldx)
        data['iterations']+=1
        data['x1'].append(new_value_fixed_point)
        data['difference'].append(differrence)
        step = step + 1

        if step > maximum_step or olddiff<differrence:
            flag = 0
            break

        condition = differrence > error_tolerance
        try:
            precision=100-abs(1-new_value_fixed_point/oldx)
        except:
            precision = 100 - differrence*100
        oldx = new_value_fixed_point

    if flag == 1:
        data['time']=time.perf_counter()*1000 - start
        data['root']=new_value_fixed_point
        data['status']='good'
        data['precision percenatge']=precision
        writeToJSONFile(data=data,name=fileName)

        return new_value_fixed_point
    else:
        data['status']='bad'
        data['exception']='notConvergent'
        writeToJSONFile(data=data,name=fileName)
        raise exceptions.notConvergent("Not convergent!")



def newton_raphson(initial_guess_newton_raphson, error_tolerance, maximum_step,newton_raphson_function,newton_raphson_rewritten_function,fileName='out/newtonOut.json'):
    createOutputFolder()
    data={'method':'newton raphson'}
    step = 1
    flag = 1
    condition = True
    data['iterations']=0
    data['x']=[]
    data['f(x)']=[]
    start = time.perf_counter()*1000
    while condition:
        if newton_raphson_rewritten_function(initial_guess_newton_raphson) == 0.0:
            data['status']='bad'
            data['exception']='ValueError'
            writeToJSONFile(data,fileName)
            raise ValueError('Divide by zero error!')
            break

        new_value_newton_raphson = initial_guess_newton_raphson - newton_raphson_function(initial_guess_newton_raphson) / newton_raphson_rewritten_function(initial_guess_newton_raphson)
        data['x'].append(new_value_newton_raphson)
        data['f(x)'].append(newton_raphson_function(new_value_newton_raphson))
        precision = 100 - abs(1-new_value_newton_raphson/initial_guess_newton_raphson)
        initial_guess_newton_raphson = new_value_newton_raphson
        data['iterations']+=1
        step = step + 1

        if step > maximum_step:
            flag = 0
            break

        condition = abs(newton_raphson_function(new_value_newton_raphson)) > error_tolerance

    if flag == 1:
        data['time']=time.perf_counter()*1000 - start
        data['status']='good'
        data['root']=new_value_newton_raphson
        data['precision']=precision
        writeToJSONFile(data,fileName)
        return new_value_newton_raphson
    else:
        data['status']='bad'
        data['exception']='notConvergent'
        writeToJSONFile(data,fileName)
        raise exceptions.notConvergent("Not convergent!")
        
def secant(xi, ximinus1, error_tolerance, maximum_step,secant_function,fileName='out/secantOut.json'):
    createOutputFolder()
    data={'method':'secant'}
    step = 1
    condition = True
    data['iterations']=0
    data['x']=[]
    data['f(x)']=[]
    start=time.perf_counter()*1000
    while condition:
        if secant_function(xi) == secant_function(ximinus1):
            data['status']='bad'
            data['exception']='ValueError'
            writeToJSONFile(data,fileName)
            raise ValueError('Divide by zero error!')
            break

        xiplus1 = xi - (ximinus1 - xi) * secant_function(xi) / (secant_function(ximinus1) - secant_function(xi))
        data['iterations']+=1
        data['x'].append(xiplus1)
        data['f(x)'].append(secant_function(xiplus1))
        xi = ximinus1
        ximinus1 = xiplus1
        step = step + 1

        if step > maximum_step:
            data['status']='bad'
            data['exception']='notConvergent'
            writeToJSONFile(data,fileName)
            raise exceptions.notConvergent("Not convergent!")
            break

        condition = abs(secant_function(xiplus1)) > error_tolerance
    data['time']=time.perf_counter()*1000 - start
    data['status']='good'
    data['root']=xiplus1
    writeToJSONFile(data,fileName)
    return xiplus1
