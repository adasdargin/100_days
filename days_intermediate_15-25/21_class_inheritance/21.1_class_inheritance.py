# Inheritance

# class Fish(Animal):
#    def __init__(self):
#        super().__init__()     # in order to get hold of all Animal's attributes & methods. Super refers to super class.

class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("inhale - exhale")


class Fish(Animal):
    # def __init__(self):
    #     super().__init__()

    def breathe(self):
        super().breathe()       # takes breathe method from class Animal
        print("diving deep")

    def swim(self):
        print("moving in the water")

nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)