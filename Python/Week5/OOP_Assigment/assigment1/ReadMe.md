# 📱 Smartphone Class in Python

This project demonstrates **Object-Oriented Programming (OOP)** concepts in Python using a `Smartphone` class and an extended `SmartphonePro` class.  
It covers **constructors, inheritance, encapsulation, and polymorphism** in a fun, practical way.

---

## 🚀 Features
- **Smartphone (Base Class):**
  - Attributes: `brand`, `model`, `storage`, `battery`
  - Methods:  
    - `power_on()` → Turns the phone ON  
    - `power_off()` → Turns the phone OFF  
    - `take_photo()` → Takes a normal photo  
    - `__str__()` → String representation of the phone  

- **SmartphonePro (Derived Class):**
  - Inherits all features from `Smartphone`
  - Adds new attribute: `stylus` (True/False)
  - Overrides `take_photo()` → Takes a PRO photo with AI features
  - Adds `use_stylus()` → Uses stylus if supported  

---

## 📝 Example Usage
```python
# Create objects
phone1 = Smartphone("Samsung", "Galaxy S22", 128, 4000)
phone2 = SmartphonePro("Apple", "iPhone 15 Pro", 256, 4500, stylus=False)

# Print phone details
print(phone1)   # Samsung Galaxy S22 (128GB, 4000mAh)
print(phone2)   # Apple iPhone 15 Pro (256GB, 4500mAh)

# Use phone1
phone1.power_on()
phone1.take_photo()

# Use phone2
phone2.power_on()
phone2.take_photo()   # Overridden method
phone2.use_stylus()   # Extra feature
