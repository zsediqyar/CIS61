# # Higher Order Functions
# # A higher function is a function that takes another function as an argument.
# Or a function that returns another function
# A functions domain is the set of all inputs it might be able to take as an arguments
# A function's range is the set of output values it might possibly return

from math import pi, sqrt


# VERSION  1
def area_square(r):
    return r * r


def area_circle(r):
    assert r > 0, "A length shall be positive" # if the r is entered a negative number, it will not run and crash.
    return r * r * pi


def area_hexagon(r):
    return r * r * 3 * sqrt(3) / 2


print(f"Area of Circle: \t {area_circle(5)}")
print(f"Area of Square: \t {area_square(5)}")
print(f"Area of Hexagon: \t {area_hexagon(5)}")


# VERSION 2 : Use DRY method (Don't Repeat Yourself)
# We find the mutual calculation point in all functions and add that in another main/general function
# We can then call the general function inside all the other functions.

def area(r, constant):
    return r * r * constant


def area_square(r):
    return area(r, 1)


def area_circle(r):
    return area(r, pi)


def area_hexagon(r):
    return area(r, 3 * sqrt(3) / 2)


print(f"Area of Circle V2: \t {area_circle(5)}")
print(f"Area of Square V2: \t {area_square(5)}")
print(f"Area of Hexagon V2: \t {area_hexagon(5)}")


# SUM NATURAL NUMBERS
# VERSION 1
def sum_naturals(n):
    """
    >>> sum_naturals(5)
    15
    """
    total = 0
    k = 1
    while k <= n:
        total = total + k
        k = k + 1
    return total


def sum_cubes(n):
    """
    >>> sum_cubes(5)
    225
    """
    total = 0
    k = 1
    while k <= n:
        total = total + pow(k, 3)
        k = k + 1
    return total


print(f"Sum of Naturals: \t {sum_naturals(5)}")
print(f"Sum of Cubes: \t {sum_cubes(5)}")


# SUM OF NATURALS
# VERSION 2 (DRY - Don't Repeat Yourself)

def summation(n, term):
    total = 0
    k = 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total


def identity(x):
    return x


def sum_naturals(n):
    return summation(n, lambda x: x)


def sum_cubes(n):
    return summation(n, lambda x: pow(x, 3))


print(f"Sum of Naturals V2: \t {sum_naturals(5)}")
print(f"Sum of Cubes V2: \t {sum_cubes(5)}")


# FUNCTIONS AS RETURN VALUES
def make_adder(n):
    def adder(k):
        return k + n
    return adder


add_four = make_adder(4)
print(add_four(5))


# RETURNING A FUNCTION USING IT'S OWN NAME
def print_sums(n):
    print(n)
    def next_sum(k):
        return print_sums(n + k)
    return next_sum


a = print_sums(10)
a(5)


