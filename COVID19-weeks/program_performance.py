'''
    PROGRAM PERFORMANCE
      
'''


def fact(n):
    if n <= 1:
        return 1
    return n * fact(n-1)


def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)


total = 0


def count(f):
    def counted_f(*args):
        global total
        total += 1
        return f(*args)
    return counted_f


# fact = count(fact)
# print(fact(30))
# print(total)

# total = 0
# fib = count(fib)
# print(fib(30))
# print(total)

# IMPROVING NUMBER OF OPERATIONS
total = 0


def fib_iter(n):
    global total
    curr, next, i = 0, 1, 0
    while i < n:
        curr, next = next, curr + next
        i += 1
        total = +1
    return curr


# iter = count(fib_iter)
# print(iter(30))
# print(total)


#   BETTER FIB FUNCTION
fib_cache = {}


def fib_memo(n):
    if n in fib_cache:
        return fib_cache[n]
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        value = fib_memo(n - 1) + fib_memo(n - 1)
        fib_cache[n] = value
    return value


# fib_memo = count(fib_memo)
# total = 0
# print(total)


#   ITERATORS AND GENERATORS
lst = [1, 2, 3, 4]
bookmark = iter(lst)
next(bookmark)
next(bookmark)
next(bookmark)
next(bookmark)


s = [1, 2, 3]
one, two = iter(s), iter(s)
# print(next(one))
# print(next(two))
# print(next(one))


def new_fib(n):
    prev, curr, i = 0, 1, 2
    lst = [curr]
    while i <= n:
        prev, curr = curr, curr + next
        i += 1
        lst += [curr]
    return iter(lst)


# x = new_fib(5)
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))


#   EXCEPTIONS / ERRORS
'''
try:
    except
'''

try:
    x = 1 / 0
except ZeroDivisionError as e:
    print('cannot divide by 0', type(e))


def slices_per_friend(cake_slice_count, friend_count):
    try:
        result = cake_slice_count / friend_count
        return result
    except ZeroDivisionError as e:
        print('You don\'t have a friend')
        return 0


slices_per_friend(10, 0)


counts = [1, 2, 3]
items = iter(counts)
# try:
#     while True:
#         item = next(items)
#         print(item)
# # except StopIteration as e
# # pass


# GENERATOR
''' A generator function is a function that contains the keyword YIELD
'''


def plus_minus(x):
    yield x
    yield -x


t = plus_minus(3)
next(t)
next(t)

lst = [1, 2, 3]


def gen_lst(lst):
    for x in lst:
        yield x


t = gen_lst(lst)
print(next(t))
print(next(t))
print(next(t))
# print(next(t))


def naturals():
    x = -1
    while True:
        x += 1
        yield x


nats1, nats2 = naturals(), naturals()


def countdown(k):
    if k == 0:
        yield 'Blass Off'
    else:
        yield k
        yield countdown(k - 1)


t = countdown(2)

i = iter([1, 2, 3, 4])


def fn(x): return x ** 2


def map_gen(fn, iter1):
    return fn(iter1)


m = map_gen(fn, i)
print(next(m))
print(next(m))
print(next(m))
print(next(m))
