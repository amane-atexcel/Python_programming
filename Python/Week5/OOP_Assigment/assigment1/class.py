# Base class
class Smartphone:
    def __init__(self, brand, model, storage, battery):
        self.brand = brand
        self.model = model
        self.storage = storage  # in GB
        self.battery = battery  # in mAh
        self.is_on = False

    def power_on(self):
        if not self.is_on:
            self.is_on = True
            print(f"{self.brand} {self.model} is now ON.")
        else:
            print(f"{self.brand} {self.model} is already ON.")

    def power_off(self):
        if self.is_on:
            self.is_on = False
            print(f"{self.brand} {self.model} is now OFF.")
        else:
            print(f"{self.brand} {self.model} is already OFF.")

    def take_photo(self):
        if self.is_on:
            print(f"📸 {self.brand} {self.model} takes a photo!")
        else:
            print("Turn on the phone first!")

    def __str__(self):
        return f"{self.brand} {self.model} ({self.storage}GB, {self.battery}mAh)"


# Derived class (Inheritance)
class SmartphonePro(Smartphone):
    def __init__(self, brand, model, storage, battery, stylus=False):
        # Call the parent constructor
        super().__init__(brand, model, storage, battery)
        self.stylus = stylus  # extra feature

    # Polymorphism: overriding method
    def take_photo(self):
        if self.is_on:
            print(f"📸 {self.brand} {self.model} takes a PRO photo with advanced AI camera!")
        else:
            print("Turn on the phone first!")

    # Extra method unique to Pro version
    def use_stylus(self):
        if self.stylus:
            print(f"{self.brand} {self.model} is using the stylus 🖊️")
        else:
            print(f"{self.brand} {self.model} does not support stylus.")


# Example usage
phone1 = Smartphone("Samsung", "Galaxy S22", 128, 4000)
phone2 = SmartphonePro("Apple", "iPhone 15 Pro", 256, 4500, stylus=False)

print(phone1)
print(phone2)

phone1.power_on()
phone1.take_photo()

phone2.power_on()
phone2.take_photo()
phone2.use_stylus()
