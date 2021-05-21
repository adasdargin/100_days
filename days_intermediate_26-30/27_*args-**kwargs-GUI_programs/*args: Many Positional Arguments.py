def add(n1, n2):
    return n1 + n2


def add_with_args(*args):
    return sum(args)           # args by default returns a tuple


print(add_with_args(1, 10, 21))