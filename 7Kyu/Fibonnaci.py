"""
Create function fib that returns n'th element of Fibonacci sequence (classic programming task).
Fundamentals
"""
#Turns out there's currently no option to solve this with Python on codewars
# I've done this a long time ago with C#, Java, and JavaScript so I made a python version which
# would work
def fibonacci(n):
    if n < 0:
        print("invalid entry")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    

print(fibonacci(4))