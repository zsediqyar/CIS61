from operator import add


# QUESTION 1
def lambda_curry2(func):
    return lambda x: lambda y: func(x, y)


curried_add = lambda_curry2(add)
add_three = curried_add(3)
# print(add_three(5))


# QUESTION 2
def keep_ints(cond, n):
    for i in range(1, n):
        if cond(i):
            print(i)


def is_even(n):
    return n % 2 == 0


# keep_ints(is_even, 5)

# QUESTION 3
def make_keeper(n):
    def keep(condition):
        for i in range(1, n):
            if condition(i):
                print(i)
    return keep


def is_even(x):
    return x % 2 == 0


make_keeper(5)(is_even)


# QUESTION 4
def and_add(f, n):
    def new_func(x):
        return f(x) + n
    return new_func


def square(x):
    return x * x


new_square = and_add(square, 3)
sample = new_square(4)

# print(sample)
