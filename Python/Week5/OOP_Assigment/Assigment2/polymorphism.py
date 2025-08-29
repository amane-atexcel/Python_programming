# Base class
class Vehicle:
    def __init__(self, name):
        self.name = name

    def move(self):
        raise NotImplementedError("Subclasses must implement this method!")

# Derived classes
class Car(Vehicle):
    def move(self):
        print(f"{self.name} is driving 🚗")

class Plane(Vehicle):
    def move(self):
        print(f"{self.name} is flying ✈️")

class Boat(Vehicle):
    def move(self):
        print(f"{self.name} is sailing 🚤")

# Example usage
vehicles = [
    Car("Tesla"),
    Plane("Boeing 747"),
    Boat("Titanic")
]

for v in vehicles:
    v.move()
