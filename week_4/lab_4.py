# QUESTION I
def skip_add(n):
    if n == 0:
        return 0
    elif n % 2 != 0:
        return n + n - 2 + n % 2
    else:
        return n + skip_add(n - 2)


print(skip_add(10))
print(skip_add(5))


# QUESTION II
def hailstone(n):
    drop_point = 1
    print(n)
    if n > 1:
        if n % 2 == 0:
            drop_point += hailstone(n // 2)
        else:
            drop_point += hailstone((n * 3) + 1)
    return drop_point


# hailstone(10)


# QUESTION III


# QUESTION IV
def isPrime(n):
    if n == 1:
        return True
    num = 2
    if num < n:
        num += 1
        return isPrime(n % num != 0)


# print(isPrime(13))
# print(isPrime(6))


# QUESTION V
def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


# print(gcd(60, 48))


# QUESTION VI
def count_stairs(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return count_stairs(n - 1) + count_stairs(n - 2)


# print(count_stairs(8))
