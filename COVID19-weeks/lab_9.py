#   IMPORTED FUNCTIONS AND CLASSES

#   for question two


class Link:
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest


#   for question three
class Tree:
    def __init__(self, entry, child=[]):
        for c in child:
            assert isinstance(c, Tree)
        self.entry = entry
        self.child = child

    def __repr__(self):
        if self.child:
            child_str = ', ' + repr(self.child)
        else:
            child_str = ''
        return 'Tree({0}{1})'.format(self.entry, child_str)

    def is_leaf(self):
        return not self.child


#   QUESTION ONE
def scale(s, k):
    yield from map(lambda x: x * k, s)

    s = scale([1, 5, 2], 5)
    type(s)
    print(list(s))


#   QUESTION TWO
def link_to_list(link):
    lst = []
    while link != Link.empty:
        lst.append(link.first)
        link = link.rest
    return lst


def link_to_list(link):
    if link == Link.empty:
        return []
    else:
        return [link.first] + link_to_list(link.rest)


# link = Link(1, Link(2, Link(3, Link(4))))
# print(link_to_list(link))
# print(link_to_list(Link.empty))


#   QUESTION THREE
def cumulative_sum(t):
    if t.is_leaf():
        pass
    else:
        for child in t.child:
            cumulative_sum(child)
            t.entry += sum([child.entry])


# t = Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
# print(t)
# cumulative_sum(t)
# print(t)


#   QUESTION FOUR
def is_bst(t):
    if t.is_leaf():
        return True
    if len(t.child) == 1:
        return True
    elif t.entry < t.child[0].entry and t.entry > t.child[1].entry:
        return False
    for c in t.child:
        return is_bst(c)


# t1 = Tree(6, [Tree(2, [Tree(1), Tree(4)]), Tree(7, [Tree(7), Tree(8)])])
# print(is_bst(t1))

# t2 = Tree(8, [Tree(2, [Tree(9), Tree(1)]), Tree(3, [Tree(6)]), Tree(5)])
# print(is_bst(t2))
