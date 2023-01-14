# Modify the add function to take an unlimited number of arguments.
# Use a loop to sum all the arguments inside the function
# Test it out by calling add() to calculate sum of some arguments
def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


print(add(2, 3, 4, 5, 7))


# **kwargs: Keyworded Variable-Length Arguments
def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


# calculate(n1=2, n2=5)
calculate(2, add=3, multiply=5)


# How to use a **kwargs dictionary safely
class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")


car = Car(make="Hyundai", model="palisade")
print(car.model)
