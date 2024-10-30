from abc import ABC, abstractmethod

class Vehicle(ABC):                      # Abstract Base Class
    def __init__(self, make, model):
        self.make = make
        self.model = model

    @abstractmethod
    def start(self):                     # Abstract method
        pass

    @abstractmethod
    def stop(self):                      # Abstract method
        pass


class Car(Vehicle):                      # Concrete subclass
    def start(self):
        print(f"{self.make} {self.model} is starting.")

    def stop(self):
        print(f"{self.make} {self.model} is stopping.")


# Trying to instantiate Vehicle directly would raise an error
# vehicle = Vehicle("Generic", "Model")  # Raises TypeError

# Instantiating the Car class and using its methods
my_car = Car("Toyota", "Corolla")
my_car.start()
my_car.stop()
