import math
import time
# Defining Function
def f(x):
    return x**3-5*x-9


def bisection(x0, x1, e,f):
    step = 1
    print('\n\n*** BISECTION METHOD IMPLEMENTATION ***')
    condition = True
    while condition:
        x2 = (x0 + x1) / 2
        print('Iteration-%d, x2 = %0.6f and f(x2) = %0.6f' % (step, x2, f(x2)))

        if f(x0) * f(x2) < 0:
            x1 = x2
        else:
            x0 = x2

        step = step + 1
        condition = abs(f(x2)) > e

    print('\nRequired Root is : %0.8f' % x2)
    return x2

# Implementing False Position Method
def falsePosition(x0,x1,e,f):
    step = 1
    print('\n\n*** FALSE POSITION METHOD IMPLEMENTATION ***')
    condition = True
    while condition:
        x2 = x0 - (x1-x0) * f(x0)/( f(x1) - f(x0) )
        print('Iteration-%d, x2 = %0.6f and f(x2) = %0.6f' % (step, x2, f(x2)))

        if f(x0) * f(x2) < 0:
            x1 = x2
        else:
            x0 = x2

        step = step + 1
        condition = abs(f(x2)) > e

    print('\nRequired root is: %0.8f' % x2)
    return x2


def h(x):
    return x * x * x + x * x - 1


# Re-writing f(x)=0 to x = g(x)
def g(x):
    return 1 / math.sqrt(1 + x)


# Implementing Fixed Point Iteration Method
def fixedPointIteration(X, E, N):
    print('\n\n*** FIXED POINT ITERATION ***')
    step = 1
    flag = 1
    condition = True
    while condition:
        xn = g(X)
        print('Iteration-%d, x1 = %0.6f and f(x1) = %0.6f' % (step, xn, h(xn)))
        X = xn

        step = step + 1

        if step > N:
            flag = 0
            break

        condition = abs(f(x1)) > E

    if flag == 1:
        print('\nRequired root is: %0.8f' % xn)
    else:
        print('\nNot Convergent.')


def newtonRaphson(X, E, N):
    print('\n\n*** NEWTON RAPHSON METHOD IMPLEMENTATION ***')
    step = 1
    flag = 1
    condition = True
    while condition:
        if g(X) == 0.0:
            print('Divide by zero error!')
            break

        xn = X - h(X) / g(X)
        print('Iteration-%d, x1 = %0.6f and f(x1) = %0.6f' % (step, xn, f(xn)))
        X = xn
        step = step + 1

        if step > N:
            flag = 0
            break

        condition = abs(f(x1)) > E

    if flag == 1:
        print('\nRequired root is: %0.8f' % x1)
    else:
        print('\nNot Convergent.')

def take_input():
    # Input Section for fixed
    X = input('Enter Guess for fixed point and Newton Raphson: ')
    E = input('Tolerable Error: ')
    N = input('Maximum Step: ')

    # Converting x0 and e to float
    X = float(X)
    E = float(E)

    # Converting N to integer
    N = int(N)

    # Input Section for bisection and false position
    x0 = input('First Guess for bisection and false position: ')
    x1 = input('Second Guess for bisection and false position: ')
    e = input('Tolerable Error for bisection and false position: ')

    # Converting input to float
    x0 = float(x0)
    x1 = float(x1)
    e = float(e)


def c(x):
    return x ** 3 - 5 * x - 9


# Implementing Secant Method

def secant(xs, xm, e1, N1):
    print('\n\n*** SECANT METHOD IMPLEMENTATION ***')
    step = 1
    condition = True
    while condition:
        if c(xs) == c(xm):
            print('Divide by zero error!')
            break

        x2 = xs - (xm - xs) * c(xs) / (c(xm) - c(xs))
        print('Iteration-%d, x2 = %0.6f and f(x2) = %0.6f' % (step, x2, c(x2)))
        xs = xm
        xm = x2
        step = step + 1

        if step > N1:
            print('Not Convergent!')
            break

        condition = abs(c(x2)) > e1
    print('\n Required root is: %0.8f' % x2)

def main():
    # Input Section
    xs = input('Enter First Guess for secant: ')
    xm = input('Enter Second Guess for secant: ')
    e1 = input('Tolerable Error for secant: ')
    N1 = input('Maximum Step for secant: ')

    # Converting x0 and e to float
    xs = float(xs)
    xm = float(xm)
    e1 = float(e1)

    # Converting N to integer
    N1 = int(N1)

    # Checking Correctness of initial guess values and false positioning
    if f(x0) * f(x1) > 0.0:
        print('Given guess values do not bracket the root.')
        print('Try Again with different guess values.')
    else:
        startfalse= time.time();
        falsePosition(x0,x1,e)
        print("time for false position is " ,time.time()-startfalse);
        startbi = time.time();
        bisection(x0,x1,e)
        print("time for bisection is ", time.time() - startbi);
        startfixed = time.time();
        fixedPointIteration(X, E, N)
        print("time for fixed is ", time.time() - startfixed);
        startnewton = time.time();
        newtonRaphson(X, E, N)
        print("time for newton raphson is ", time.time() - startnewton);

        startsecant=time.time();
    secant(xs,xm,e1,N1)
    print("time for secant is ", time.time() - startsecant);