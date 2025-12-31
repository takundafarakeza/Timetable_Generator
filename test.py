import math


def scale_down(limit, num):
    return num - limit * (math.ceil(num / limit) - 1)


print(scale_down(6, 348))
