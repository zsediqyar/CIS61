# # FUNCTION ABSTRACTION
# Mechanics of a function:
# A function is executed line by line
# RECURSION & ITERATION


def fact(n):
    if n == 1:
        return 1
    else:
        return fact(n - 1) * n


print(fact(5))


# Structure of Recursive function
# It has one or more base cases, usually the smallest input
# One or more ways of reducing the problem then solving the smaller problems using recursion


# COUNT UP FUNCTION USING RECURSION
def count_up(n):
    if n == 1:
        print(1)
    else:
        count_up(n - 1)
        print(n)


count_up(5)


# SUM DIGITS RECURSION
def sum_digits(n):
    if n < 10:
        return n
    else:
        last = n % 10
        rest = n // 10
        return sum_digits(rest) + last


print(sum_digits(2019))

# CASCADE
# Print out a cascading tree of positive integer n


def cascade(n):
    if n < 10:
        print(n)
    else:
        print(n)
        cascade(n // 10)
        print(n)


cascade(4866842)


# FIBONACCI SEQUENCE IN RECURSION
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 2) + fib(n - 1)


print(fib(6))


# COUNTING PARTITIONS
def count_part(number_of_pieces, max_give_away):
    if number_of_pieces < 0:
        return 0
    else:
        with_max = count_part(number_of_pieces - max_give_away, max_give_away)
        without_max = count_part(number_of_pieces, max_give_away - 1)
        return with_max + without_max
