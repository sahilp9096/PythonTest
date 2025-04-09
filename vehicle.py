# Base class
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

# Derived class (Inheritance)
class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)  # Calling the constructor of the base class
        self.__doors = doors  # Private attribute (Encapsulation)

    def display_info(self):
        super().display_info()
        print(f"Number of doors: {self.__doors}")

    # Getter method for private attribute
    def get_doors(self):
        return self.__doors

    # Setter method for private attribute
    def set_doors(self, doors):
        if doors > 0:
            self.__doors = doors
        else:
            print("Number of doors must be positive.")

# Creating objects
vehicle1 = Vehicle("Honda", "Civic")
vehicle1.display_info()

print()

car1 = Car("Toyota", "Corolla", 4)
car1.display_info()

# Updating private attribute using setter
car1.set_doors(2)
print("\nUpdated Car Info:")
car1.display_info()
