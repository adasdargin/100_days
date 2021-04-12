# def function_a(smth):
#     do this with smth
#     then do this
#     finally do this

# def function_b():
#     do this


# function_a(function_b)   we pass the second function without the parentheses at the end.

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2

#higher order functions
def calculator(n1, n2, func):
    return func(n1, n2)


result = calculator(2, 3, add)
print(result)