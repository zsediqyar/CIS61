from operator import add, sub

# QUESTION 1
def both_positive(x, y):
    return x > 0 and y > 0


print(both_positive(1, 6))


# QUESTION 2
def a_plus_abs_b(a, b):
    if b < 0:
        f = sub
    else:
        f = add
    return f(a, b)


print(a_plus_abs_b(1, -5))


# QUESTION 3
def two_of_three(a, b, c):
    return max(a*a+b*b, a*a+c*c, b*b+c*c)


print(two_of_three(5, 3, 1))


# QUESTION 4
def largest_factor(n):
    factor = n - 1
    while factor > 0:
        if n % factor == 0:
            return factor
        factor -= 1

print(largest_factor(15))
print(largest_factor(80))


# QUESTION 5
def sum_digits(n):
    number = n
    result = 0
    while number > 0:
        remainder = number % 10
        result += remainder
        number = number // 10
    return result


print(sum_digits(123))


# QUESTION 6
def hailstone(n):
    drop_point = 1
    while n != 1:
        print(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
            drop_point = drop_point + 1
    print(n)


hailstone(10)


# QUESTION 7
def fibonacciN(n):
    old_val = 0
    curr_val = 1
    if n < 0:
        print(f"{n} is an incorrect number")
    elif n == 1:
        return curr_val
    else:
        for i in range(1, n):
            fib_value = old_val + curr_val
            old_val = curr_val
            curr_val = fib_value
        return  curr_val


print(fibonacciN(5))
print(fibonacciN(7))


# QUESTION 8
def is_prime(n):
    if n == 1:
        return True
    num = 2
    while num < n:
        if n % num == 0:
            return False
        num += 1
    return True


print(is_prime(13))
print(is_prime(15))
