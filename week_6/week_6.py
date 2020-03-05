"""
SEQUENCE AGGREGATION:
Iterable => an object capable of returning it's members one at a time
"""

'''
TREES

Tree Abstraction: 
Tree is a hierarchical data structure

'''


# CONSTRUCTOR
def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch)
        return [label] + list[branches]


# CONSTRUCTORS
def label(tree):
    return tree[0]


def branches(tree):
    return tree[1:]


def is_tree(tree):
    if type(tree) == list and len(tree) > 0:
        return True
    else:
        return False


def is_leaf(tree):
    return not branches(tree)


t1 = tree(3, [tree(1), ])

'''
TREE PROCESSING USING RECURSION
'''
# COUNT NODES IN A TREE
sample = [
    [
        [2, 3]
        [1, [
            [1, 1]
        ]]
    ]
]


def count_nodes(t):
    if is_leaf(t):
        return 1
    total = 0
    for b in branches(t):
        total += count_nodes(b)
    return total


def count_nodes_2(t):
    if is_leaf(t):
        return 1

    lst = [count_nodes_2(b) for b in branches(t)]


# COLLECT THE LEAVES IN A TREE RECURSIVELY
def collect_leaves(t):
    if is_leaf(t):
        return [label(t)]
    leaves = []
    for b in branches(t):
        leaves += collect_leaves(b)
    return leaves


# PRINT TREE VISUALLY
li = [3, [1, [0], [1]], [2, [1], [1, [0], [1]]]]


def print_tree(t):
    for i in range(len(t)):
        print(t[i])


print_tree(li)


# CREATING A NEW TREE FROM ANOTHER TREE RECURSIVELY
def square_tree(t):
    if is_leaf(t):
        return tree(label(t) ** 2)
    lst = []
    for b in branches(t):
        lst = lst + [square_tree(b)]
    return tree(label(t) ** 2, lst)


square_tree(li)


# FIBONACCI TREE WITH RECURSION
def fib_tree(n):
    if n == 0:
        return tree(0)
    elif n == 1:
        return tree(1)
    else:
        left = fib_tree(n - 2)
        right = fib_tree(n - 1)
        lab = label(left) + label(right)
        return tree(lab, [left, right])
