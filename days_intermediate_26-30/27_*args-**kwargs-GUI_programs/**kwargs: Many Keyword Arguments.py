def calculate(n, **kwargs):
    print(kwargs)           # kwargs by default returns a dictionary
    n += kwargs["add"]
    n /= kwargs["divide"]
    print(n)


calculate(2, add=3, divide=4)   # 1.25




class Car:
    def __init__(self, **kwargs):
        # self.make = kwargs["make"]
        # self.model = kwargs["model"]

        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")


my_car = Car(model="GTR")
print(my_car.make)          # None
print(my_car.model)         # GTR