# 🚙✈️🚤 Vehicle Polymorphism in Python

This project demonstrates **polymorphism** in Python using a base `Vehicle` class and derived classes `Car`, `Plane`, and `Boat`.  
Each subclass defines the same action (`move()`), but with different behaviors.

---

## 🚀 Features
- **Base Class: `Vehicle`**
  - Contains a `move()` method placeholder (forces subclasses to define it).  

- **Derived Classes:**
  - `Car.move()` → `"Driving 🚗"`
  - `Plane.move()` → `"Flying ✈️"`
  - `Boat.move()` → `"Sailing 🚤"`

---

## 📝 Example Code
```python
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
