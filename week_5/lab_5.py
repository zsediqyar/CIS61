from math import sqrt


# QUESTION ONE
def if_this_not_that(i_list, this):
    for i in range(len(i_list)):
        if i_list[i] > this:
            print(i_list[i])
        else:
            print("that")


sample = [1, 2, 3, 4, 5]
if_this_not_that(sample, 3)


# QUESTION TWO
def couple(list_one, list_two):
    sample = []
    for i in range(len(list_one)):
        sample.append([list_one[i], list_two[i]])
    return sample


s = [1, 2, 3]
b = [4, 5, 6]

print(couple(s, b))


# QUESTION THREE
def enumerate(s, start=0):
    new_list = []
    for i in range(len(s)):
        new_list.append([s[i], start])
    return new_list


print(enumerate('five', 5))


# QUESTION FOUR
def squares(n):
    new_list = []
    for i in range(len(n)):
        if round(n[i] ** 0.5) ** 2 == n[i]:
            new_list.append(int(sqrt(n[i])))
    return new_list


seq = [8, 49, 8, 9, 2, 1, 100, 102]

print(squares(seq))


# QUESTION FIVE


# QUESTION SIX
def flatten(lst):
    flat_list = []
    for items in lst:
        if type(items) is list:
            flat_list.extend(items)
        else:
            flat_list.append(items)
    return flat_list


x = [1, [2, 3], 4]
print(flatten(x))

# QUESTION SEVEN
# QUESTION EIGHT
# QUESTION NINE
