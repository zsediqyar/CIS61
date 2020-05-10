#   QUESTION ONE
def add_this_many(x, el, lst):
    """ Adds el to the end of lst the number of times x occurs in lst. 
    >>> lst = [1, 2, 4, 2, 1]
    >>> add_this_many(1, 5, lst)
    >>> lst [1, 2, 4, 2, 1, 5, 5]
    >>> add_this_many(2, 2, lst)
    >>> lst [1, 2, 4, 2, 1, 5, 5, 2, 2]
    """
    i = 0
    while i < x:
        lst.append(el)
        i += 1


#   QUESTION ONE TEST
# lst = [1, 2, 4, 2, 1]
# print(lst)
# add_this_many(1, 5, lst)
# print(lst)
# add_this_many(2, 2, lst)
# print(lst)


#   QUESTION TWO
def group_by(s, fn):
    grouped = {}
    for x in s:
        key = fn(x)
        if key in grouped:
            grouped[key].append(x)
        else:
            grouped[key] = [x]
    return grouped


#   QUESTION TWO TEST
# print(group_by([12, 23, 14, 45], lambda p: p // 10))
# print(group_by(range(-3, 4), lambda x: x * x))


#   QUESTION THREE
def make_adder_inc(n):
    def add(x):
        nonlocal n
        n += 1
        return x + n - 1
    return add


#   QUESTION THREE TEST
# adder1 = make_adder_inc(5)
# adder2 = make_adder_inc(6)
# print(adder1(2))  # 7
# print(adder1(2))  # 8
# print(adder1(10))  # 17


#   QUESTION FIVE
def memory(n):
    """ >>> f = memory(10) 
    >>> f(lambda x: x * 2) 
    20 
    >>> f(lambda x: x - 7) 
    13 
    >>> f(lambda x: x > 5) 
    True 
    """
    def f(g):
        nonlocal n
        n = g(n)
        return n
    return f


#   QUESTION FIVE TEST
f = memory(10)
# print(f(lambda x: x * 2))
# print(f(lambda x: x - 7))
# print(f(lambda x: x > 5))


#   QUESTION SIX
def make_fib():
    current = 0
    next = 1

    def fib():
        nonlocal current, next
        result = current
        current, next = next, current + next
        return result
    return fib


#   QUESTION SIX TEST
# fib = make_fib()
# print(fib())
# print(fib())
# print(fib())
# print(fib())
# print(fib())
# fib2 = make_fib()
# print(fib() + sum([fib2() for _ in range(5)]))


#   QUESTION SEVEN
def make_withdraw(balance, password):
    password_list = []
    count = 0

    def withdraw(amount, p):
        nonlocal count, balance
        if count == 3:
            return 'Your account is locked. Attempts: ' + str(l)
        if p != password:
            password_list.append(p)
            count += 1
            return 'Incorrect password'
        if amount > balance:
            return 'Insufficient funds'
            balance -= amount
        return balance
    return withdraw


#   QUESTION SEVEN TEST
# w = make_withdraw(100, 'hax0r')
# print(w(25, 'hax0r'))
# error = w(90, 'hax0r')
# print(error)
# error = w(25, 'hwat')
# print(error)
# new_bal = w(25, 'hax0r')
# print(new_bal)
# print(w(75, 'a'))
# print(w(10, 'hax0r'))
# print(w(20, 'n00b'))
# print(w(10, 'hax0r'))
# print(w(10, 'l33t'))
# print(type(w(10, 'l33t')) == str)


#   QUESTION EIGHT
def make_joint(withdraw, old_password, new_password):
    """Return a password-protected withdraw function that has joint access to
    the balance of withdraw.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> make_joint(w, 'my', 'secret')
    'Incorrect password'
    >>> j = make_joint(w, 'hax0r', 'secret')
    >>> w(25, 'secret')
    'Incorrect password'
    >>> j(25, 'secret')
    50
    >>> j(25, 'hax0r')
    25
    >>> j(100, 'secret')
    'Insufficient funds'

    >>> j2 = make_joint(j, 'secret', 'code')
    >>> j2(5, 'code')
    20
    >>> j2(5, 'secret')
    15
    >>> j2(5, 'hax0r')
    10

    >>> j2(25, 'password')
    'Incorrect password'
    >>> j2(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> j(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> w(5, 'hax0r')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> make_joint(w, 'hax0r', 'hello')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    """
    "*** YOUR CODE HERE ***"
    error = withdraw(0, old_password)
    if type(error) == str:
        return error

    def joint(amount, attempt):
        if attempt == new_password:
            return withdraw(amount, old_password)
        else:
            return withdraw(amount, attempt)
    return joint


#   QUESTION EIGHT TEST
w = make_withdraw(100, 'hax0r')
print(w(25, 'hax0r'))
print(make_joint(w, 'my', 'secret'))
# EXPECTING --> 'Incorrect password'
