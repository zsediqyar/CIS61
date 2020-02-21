# WEEK 2 OF THE LECTURES - CIS61
# FIB sequence


def fib(n):
    prev, curr = 0, 1
    k = 0
    while k < n:
        prev, curr = curr, prev + curr
        k = k + 1
        print(curr, " ", prev)
    return prev


fib(9)


# Lambda Expressions
# normal function
def square(x):
    return x * x


# lambda expressions
lamb = lambda x: x * x


print("this is lambda ", lamb(5))


