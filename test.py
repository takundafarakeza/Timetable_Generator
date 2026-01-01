import math


def scale_down(limit, num):
    return num - limit * (math.ceil(num / limit) - 1)


def numberize(base, num):
    print(math.floor(num / 10) + 1)
    num_scaled = scale_down((math.floor(num / 10) + 1) * 10, num)
    num_scaled = math.ceil(num_scaled / 10)
    multiplier = 10 ** (math.floor(num_scaled / 10) + 1)
    return base * multiplier + num


print(numberize(111, 67))

