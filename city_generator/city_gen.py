import random

city_sizes = {"village": (25, 100), "town": (101, 500),
              "large town": (501, 1000), "city": (1001, 3000),
              "large city": (3001, 5000), "metropolis": (5001, 10000)}

with open("city_name_syllables.txt") as f:
    city_name_syllables = f.read().splitlines()

len_city_syllables = len(city_name_syllables)


def random_city_size():
    """
    Returns a tuple of type (string, int),
    representing the type of city and it's
    population
    """
    city_type = random.choice(city_sizes.keys())

    lower_size_bound = city_sizes[city_type][0]
    upper_size_bound = city_sizes[city_type][1]

    city_size = random.randrange(lower_size_bound, upper_size_bound)

    return city_type, city_size


def simple_city_name():
    """
    Returns a random city name, with component syllables drawn from
    city_name_syllables.txt
    """

    return pattern_city_name("{U}{}")


def city_name(syllables):
    """
    n-syllable name city name
    param: syllables should be type int
    """

    rand1 = random.randrange(len_city_syllables)
    first = city_name_syllables[rand1]
    last = []

    for i in range(syllables):
        n = random.randrange(len_city_syllables)
        last.append(city_name_syllables[n].lower())

    last = "".join(last)
    return first + last


def random_city(syllables):
    name = city_name(syllables)
    city_type = random_city_size()
    size = city_type[0]
    population = city_type[1]

    return "{}, a {} with a population of {}".format(name, size, population)


def ornate_city_name_1():
    """
    Returns a city name, stylized as C'Cc, where C is a capitalized
    syllable drawn from city_name_syllables and Cc is drawn from
    simple_city_name()
    """

    return pattern_city_name("{U}'{}{}")


def ornate_city_name_2():
    return pattern_city_name("{U}-{}")


def pattern_city_name(pattern):
    """
    Returns a city name, stylized with an arbitrary pattern, where
    {U} gives a capital syllable and {} gives a lower case syllable.
    """

    for symbol in ["{U}", "{}"]:
        while symbol in pattern:
            rand = random.randrange(len_city_syllables)
            if symbol is "{U}":
                new_syllable = city_name_syllables[rand]
            else:
                new_syllable = city_name_syllables[rand].lower()
            pattern = pattern.replace(symbol, new_syllable, 1)
    return pattern


def simple_random_city():
    """
    Returns a two-syllable, non-stylized random city name
    """

    name = simple_city_name()
    city_type = random_city_size()

    size = city_type[0]
    population = city_type[1]

    return "{}, a {} with a population of {}".format(name, size, population)
