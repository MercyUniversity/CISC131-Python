class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year

    # Class method: Creates a Car instance from a string
    @classmethod
    def from_string(cls, car_str):
        model, year = car_str.split('-')
        return cls(model, int(year))

    # Static method: Checks if a given year makes the car "classic"
    @staticmethod
    def is_classic(year):
        return year < 1990

# Usage of Class Method
# The from_string method uses the class itself (cls) to create an instance
# Here, we create car1 from a string rather than passing model and year directly
car1 = Car.from_string("Mustang-1967")
print(f"Model: {car1.model}")  # Output: Mustang
print(f"Year: {car1.year}")    # Output: 1967

# Usage of Static Method
# The is_classic method can be used without creating a Car instance
# It simply takes a year as input and returns whether it is considered classic
print(Car.is_classic(car1.year))  # Output: True

# Alternative usage of Static Method
# We can also use it independently of any instance, since it does not rely on `self` or `cls`
print(Car.is_classic(2000))       # Output: False
print(Car.is_classic(1985))       # Output: True
