from doctest import testmod
from math import pi



# Q1
def twenty_twenty():
  return 10 + 10 + (10 * 10 * 4 * 5)

print(twenty_twenty())


# Q2
def sphere_area(r):
  return 4 * pi * (r * r)


def sphere_volume(r):
  return 4 / 3 * pi * (r * r * r)

print(sphere_area(4))
print(sphere_volume(4))


# Q3
def wears_jacket(temp, raining):
    """
    >>> wears_jacket(90, False)
    False
    >>> wears_jacket(40, False)
    True
    >>> wears_jacket(100, True)
    True
    """
    if raining or temp < 60:
        return True
    else:
        return False


if __name__ == '__main__':
    testmod(name='wears_jacket', verbose=True)

# Q4
def sumN(n):
    total  = 0
    for numbers in range(n):
        total = total + numbers + 1
    print(f"The Total Is: {total}")

sumN(5)
sumN(3)
