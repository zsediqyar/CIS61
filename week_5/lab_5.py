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

# QUESTION SEVEN (OPTIONAL)


# QUESTION EIGHT
def make_city(name, lat, lon):
    return [name, lat, lon]


def get_name(s):
    return s[0]


def get_lat(s):
    return s[1]


def get_lon(s):
    return s[2]


def distance(city1, city2):
    city_1_lat = get_lat(city1)
    city_1_lon = get_lon(city1)
    city_2_lat = get_lat(city2)
    city_2_lon = get_lon(city2)
    dis = sqrt(((city_1_lat - city_2_lat) ** 2) +
               ((city_1_lon - city_2_lon) ** 2))
    return dis


Berkeley = make_city('Berkeley', 6.5, 12)
Sacramento = make_city('Sacramento', 2.5, 15)

print(distance(Berkeley, Sacramento))


# QUESTION NINE
berkeley = make_city('Berkeley', 37.87, 112.26)
stanford = make_city('Stanford', 34.05, 118.25)


def closer_city(lat, lon, city1, city2):
    city_1_lat = get_lat(city1)
    city_1_lon = get_lon(city1)
    city_2_lat = get_lat(city2)
    city_2_lon = get_lon(city2)
    city_1_distance = sqrt(((lat - city_1_lat) ** 2) +
                           ((lon - city_1_lon) ** 2))
    city_2_distance = sqrt(((lat - city_2_lat) ** 2) +
                           ((lon - city_2_lon) ** 2))

    if city_1_distance < city_2_distance:
        return city1[0]
    else:
        return city2[0]


print(closer_city(38.33, 121.44, berkeley, stanford))
