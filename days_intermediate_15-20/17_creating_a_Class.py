class Car:
    # initialise attributes
    def __init__(self, seats):      # self stands for object to put in place
        self.seats = seats

    #Method
    def enter_race_mode(self):
        self.seats = 2

my_car = Car(5)
# the same as
my_car.seats = 5

my_car.enter_race_mode()