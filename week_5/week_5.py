''' 
*********** SEQEUENCES *************
- A Sequence is an ordered collection of values.
- A list is a sequence of values of any type of data.
- A LIST in Python is like an ARRAY in other languages like C++ or Java or Javascript. But it is not strongly typed. Meaning, a list in Python can contain any data type at the same time, it doesn't have to be one specific data type. 

*********** SEQEUENCE ABSTRACTION *************
- All sequences have finite length, and each element in a sequence has a discrete integer index. 
- Elements are retrieveable at a particular position
- Create and copy a subsequence

*********** SEQEUENCE PROCESSING *************

'''
lst = [1, 2, 3, 4, 5, 6]

# PRINTS THE ELEMENTS FROM THE INDEXS
for i in range(len(lst)):
    print(lst[i])

# PRINTS THE ELEMENTS FROM THE VALUES
for i in lst:
    print(i)

i = 0
for elem in [8, 9, 10]:
    print(i, ":",  elem)
    i += 1

'''
*********** LIST COMPREHENSIONS *************
You can create a list out of a sequence using list comprehensions
'''

lst = []
for i in range(10):
    lst = lst + [i]
print(lst)

lst_2 = [x for x in range(5)]
print(lst_2)


lst_3 = [x * 5 for x in range(10) if x % 2 == 0]
print(lst_3)


lst_4 = [c + "0" for c in "cis61"]
print(lst_4)


'''
*********** DICTIONARIES *************
A Dictionary is like an object in JavaScript, elements with key value pairs.
'''
user = {"name": "test", "password": 1234}
print(user["name"])

nums = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four'
}

print(nums[1])


'''
*********** DATA ABSTRACTION *************
- Compound values combine other values together
- A data: a year, a month, a day
- Data abstraction let us manipulate compound values as units. It isolates two parts of any program that use data.
    - how data are represented (as parts)
    - how data are manipulated (as units)
'''

# def mul_rational(x, y):
#     return rational(num(x) * number(y), denom(x) * denom(y))


# def add_rational(x, y):
#     nx, dx = numer(x), denom(x)
#     ny, dy = numer(x), denom(y)
#     return rational(nx * dy + ny * dx, dx * dy)

def rational(n, d):
    return [n, d]


def numer(x):
    return x[0]


def denom(x):
    return x[1]


def mul_rational(x, y):
    # the product of rational numebers X & Y
    nx, dx = numer(x), denom(x)
    ny, dy = numer(y), denom(y)
    return rational(nx * ny, dx * dy)


def add_rational(x, y):
    # the sum of rational numbers X & Y
    nx, dx = numer(x), denom(x)
    ny, dy = numer(y), denom(y)
    n = nx * dy + dx * ny
    d = dx * dy
    return rational(n, d)


def print_rational(x):
    print(numer(x), "/", denom(x))


def rationals_are_equal(x, y):
    # checks whether rational numbers X & Y are equal, then returns True
    return numer(x) * denom(y) == numer(y) * denom(x)


r1 = rational(2, 2)
r2 = rational(2, 3)
print_rational(r1)
print_rational(r2)

add_rational(r1, r2)
print(add_rational(r1, r2))

mul_rational(r1, r2)
print(mul_rational(r1, r2))


rationals_are_equal(r1, r2)
print(rationals_are_equal(r1, r2))


'''
*********** ABSTRACTION BARRIERS*************

'''
