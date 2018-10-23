"""
CP1404/CP5632 Practical
Recursion
"""


def do_it(n):
    """Do... it."""
    if n <= 0:
        return 0
    return n % 2 + do_it(n - 1)


# print(do_it(5))
# TODO: 1. write down what you think the output of this will be,
# Expected output: n = 5. 1
"""
n = 5. 1
n = 4. 1
n = 3. 2
n = 2. 2
n = 1. 3
"""
# TODO: 2. use the debugger to step through and see what's actually happening


def do_something(n):
    """Print the squares of positive numbers from n down to 0."""
    if n < 0:
        return 0
    print(n ** 2)
    do_something(n - 1)

# TODO: 3. write down what you think the output of do_something(4) will be,
# Expected output 5,4,3,2,1,0,1,4. Output is infinite.
# TODO: 4. use the debugger to step through and see what's actually happening
do_something(4)

# TODO: 5. fix do_something() so that it works according to the docstring

