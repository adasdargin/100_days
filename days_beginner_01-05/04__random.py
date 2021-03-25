import random

random_integer = random.randint(1, 10)
print(random_integer)


random_float = random.random()
#duoda float tarp 0 ir 1, neįskaitant 1.
#0.000000 - 0.99999999
print(random_float)

random_float_mpl = random_float * 5
#0.0000000 - 4.9999999
print(random_float_mpl)