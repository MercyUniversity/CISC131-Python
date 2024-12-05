class Car:
    def __init__(self, make, model):
        self.make = make                 # Public attribute
        self.model = model               # Public attribute
        self._engine_status = "Off"      # Protected attribute
        self.__mileage = 0               # Private attribute (name mangling)

    def start_car(self):                 # Public method
        self._engine_status = "On"
        print(f"The {self.make} {self.model} is starting.")
        # Calls private method to update mileage
        self.__update_mileage(10)

    def _check_engine(self):             # Protected method
        return self._engine_status == "On"

    def __update_mileage(self, miles):   # Private method
        if self._check_engine():
            self.__mileage += miles
            print(f"Mileage updated to {self.__mileage} miles.")
        else:
            print("Engine is off. Cannot update mileage.")


# Instantiating the Car class
my_car = Car("Toyota", "Corolla")

# # Accessing public attributes and methods
print(my_car.make)                 # Accessible
my_car.start_car()                 # Accessible

# # Accessing protected attribute and method (not recommended)
print(my_car._engine_status)       # Accessible, but use with caution
print(my_car._check_engine())      # Accessible, but use with caution

# # Trying to access private attribute and method
# try:
#     # print(my_car.__mileage)          # Raises AttributeError
#     my_car.__update_mileage(50)      # Raises AttributeError
# except AttributeError as e:
#     print(e)
    
# # Accessing private attribute and method using name mangling (not recommended)
print(my_car._Car__mileage)        # Accessible via name mangling
my_car._Car__update_mileage(20)    # Accessible via name mangling
