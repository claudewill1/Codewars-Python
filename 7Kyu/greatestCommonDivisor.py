"""
Find the greatest common divisor of two positive integers. The integers can be large, so you need to find a clever solution.

The inputs x and y are always greater or equal to 1, so the greatest common divisor will always be an integer that is also greater or equal to 1.
Algorithms
Optimization
Fundamentals
Recursion
Computability Theory
Theoretical Computer Science
"""

"""
On one test this solution causes problems:

def mygcd(x, y):
    if x == 0 or x == y:
        return y
    if y == 0:
        return x
    if x == y:
        return y
    if x > y:
        return mygcd(x-y, y) 
    return mygcd(x,y-x)

"""

# Final Solution
def mygcd(x, y):
    if y == 0:
        return x
    else:
        return mygcd(y,x%y)