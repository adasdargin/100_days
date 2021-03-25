# Review:
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.
def greet():
    print("Hello")
    print("How are you?")
    print("Is the weather nice today?")

greet()

#Function that allows for input:
def greet_with_name(name): #name yra parametras
    print(f"Hello {name}")
    print(f"How are you {name}?")

greet_with_name("Adas") #Adas yra argumentas

#Functions with more than 1 input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What's it like in {location}?")

greet_with("Jack", "Barcelona")

#Functions with keyword arguments
greet_with(location="Valencia", name="Gloria")