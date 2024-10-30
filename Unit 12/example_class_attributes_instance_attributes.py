class Car:
    brand = "Toyota"  # Class attribute

    def __init__(self, model, color):
        self.model = model  # Instance attribute
        self.color = color  # Instance attribute

# Create two instances of the Car class
car1 = Car("Camry", "Silver")
car2 = Car("Corolla", "Blue")

# Accessing class and instance attributes
print(car1.brand)  # Output: Toyota
print(car2.brand)  # Output: Toyota
print(car1.model)  # Output: Camry
print(car2.model)  # Output: Corolla

# Modifying an instance attribute
car1.color = "Black"
print(car1.color)  # Output: Black
print(car2.color)  # Output: Blue
