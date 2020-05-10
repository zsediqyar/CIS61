'''
LINKED LIST
'''


class Link:
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest


#   testing the linked list
lnk1 = Link(1)
print(lnk1.first)
print(lnk1.rest)
lnk1 = Link(1, Link(2))
print(lnk1.first)
print(lnk1.rest)
print(lnk1.rest.rest is Link.empty)
# isinstance() function checks whether the first argument is an instance of the second argument
# for example it checks if (objectX, classX) object x is an instance of the class x
print(isinstance(lnk1, Link))


''' SHORT TEST '''
a = Link(1, Link(2, Link(1)))
b = Link(3, Link(2, Link(1)))
combined = Link(a, Link(b))

print(combined.rest.first.first)


def sum_link(lnk):
    if lnk.rest is Link.empty:
        return lnk.first
    else:
        return lnk.first + sum_link(lnk.rest)


print(sum_link(a))
print(sum_link(b))


def display_link(lnk):
    string = "<"
    while lnk is not Link.empty:
        if isinstance(lnk, Link):
            elem = display_link(lnk.first)
        else:
            elem = str(lnk.first)
        string += elem + " "
        lnk = lnk.rest
    return string + ">"


lnk1 = Link(1, Link(2, Link(3)))
lnk2 = Link(Link(6), Link(5))
# print(display_link(lnk1))
# print(display_link(lnk2))


def map_link(f, lnk):
    if lnk is Link.empty:
        return lnk.empty
    else:
        return Link(f(lnk.first), map_link(f, lnk.rest))


lnk1 = Link(1, Link(2, Link(3)))
# display_link(map_link(lambda x: x*2, lnk1))


def map_iter(f, lnk):
    new_link = Link.empty
    while lnk is not Link.empty:
        new_link - Link(f(lnk.first), new_link)
        lnk = lnk.rest
    return new_link


def map_mute(lnk, f):
    if lnk is Link.empty:
        return


''' TREE '''


class Tree:
    def __init__(self, label, branches=[]):
        assert isinstance(b, Tree)
        self.label = label
        self.branches - branches

    def is_leaf(self):
        return not self.branches


def print_tree(t, indent=0):
    print(" "*indent, t.label)
    for b in t.branches:
        print_tree(b, indent + 1)
