# ****************************** BEGIN TREE CONSTRUCTORS *********************************
def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch)
    return [label] + list(branches)


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


def count_nodes(t):
    if is_leaf(t):
        return 1
    total = 0
    for b in branches(t):
        total += count_nodes(b)
    return total + 1


def count_nodes_2(t):
    lst = [count_nodes_2(b)
           for b in branches(t)]
    return sum(lst, 1)


def collect_leaves(t):
    if is_leaf(t):
        return [label(t)]
    leaves = []
    for b in branches(t):
        leaves += collect_leaves(b)
    return leaves


def collect_leaves_2(t):
    if is_leaf(t):
        return [label(t)]
    leaves = [collect_leaves_2(b)
              for b in branches(t)]
    return sum(leaves, [])


def print_tree(t, indent=0):
    if is_leaf(t):
        print(" "*indent, label(t))
    else:
        print(" "*indent, label(t))
    for b in branches(t):
        print_tree(b, indent + 1)


# ****************************** END OF TREE CONSTRUCTORS *********************************


# QUESTION ONE
def acorn_finder(t):
    if label(t) == 'acorn':
        return True
    for b in branches(t):
        if acorn_finder(b):
            return True
    return False


sproul = tree(
    'roots', [tree('branch1', [tree('leaf'), tree('acorn')]), tree('branch2')])
# print(acorn_finder(sproul))


# QUESTION TWO
def prune_leaves(t, values):
    if is_leaf(t) and (label(t) in values):
        return None
    new_branches = []
    for b in branches(t):
        new_branch = prune_leaves(b, values)
        if new_branch:
            new_branches += [new_branch]
    return tree(label(t), new_branches)


t = tree(2)
# print(prune_leaves(t, (1, 2)))


# QUESTION THREE
def sprout_leaves(t, items):
    if is_leaf(t):
        return tree(label(t), [tree(v) for v in items])
    return tree(label(t), [sprout_leaves(b, items) for b in branches(t)])


t1 = tree(1, [tree(2), tree(3)])
new1 = sprout_leaves(t1, [4, 5])
# print_tree(new1)


# QUESTION FOUR
def height(t):
    if is_leaf(t):
        return 1
    total = 0
    for b in branches(t):
        total += height(b)
    return total


t = tree(3, [tree(5, [tree(1)]), tree(2)])
# print(height(t))


# QUESTION FIVE
def double_tree(t):
    if is_leaf(t):
        return tree(label(t) * 2)
    lst = []
    for b in branches(t):
        lst = lst + [double_tree(b)]
    return tree(label(t) * 2, lst)


numbers = tree(1, [tree(2, [tree(3), tree(4)]),
                   tree(5, [tree(6, [tree(7)]), tree(8)])])
print_tree(double_tree(numbers))
