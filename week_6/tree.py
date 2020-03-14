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
