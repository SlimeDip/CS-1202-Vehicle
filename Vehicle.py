from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self):
        self._name = None
        self._speed = 0
        self._fuel = 0
        self._max_fuel = 0
        self._fuel_type = None
        # add nalang kayo ng mga attributes na gusto nyo

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value

    @property
    def speed(self):
        return self._speed
    
    @speed.setter
    def speed(self, value):
        if value < 0:
            raise ValueError("Speed cannot be negative")
        self._speed = value

    @property
    def fuel(self):
        return self._fuel
    
    @fuel.setter
    def fuel(self, value):
        if value < 0:
            raise ValueError("Fuel cannot be negative")
        self._fuel = value
        self._max_fuel = value

    @property
    def fuel_type(self):
        return self._fuel_type
    
    @fuel_type.setter
    def fuel_type(self, value):
        if value.lower() not in ["gasoline", "diesel", "electric"]:
            raise ValueError("Invalid fuel type")
        self._fuel_type = value

    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

    @abstractmethod
    def drive(self, amount):
        pass

    @abstractmethod
    def refuel(self, amount):
        pass

    # add nalang kayo ng mga methods na gusto nyo

# itong Car na ito ay example lang
class Car(Vehicle):
    def start_engine(self):
        print("Car engine started")

    def stop_engine(self):
        print("Car engine stopped")

    def drive(self, amount):
        if self._fuel <= 0:
            print("Cannot drive, fuel is empty")
            return
        self._fuel -= amount
        print(f"Driving car, remaining fuel: {self._fuel}/{self._max_fuel}")

    def refuel(self):
        self._fuel = self._max_fuel
        print(f"Car refueled: {self._fuel}/{self._max_fuel}")

class Motorcycle(Vehicle):
    def start_engine(self):
        print("Motorcycle engine started")

    def stop_engine(self):
        print("Motorcycle engine stopped")

    def drive(self, amount):
        if self._fuel <= 0:
            print("Cannot drive, fuel is empty")
            return
        self._fuel -= amount
        print(f"Driving motorcycle, remaining fuel: {self._fuel}/{self._max_fuel}")

    def refuel(self):
        self._fuel = self._max_fuel
        print(f"Motorcycle refueled: {self._fuel}/{self._max_fuel}")

def create_vehicle():
    print("Select vehicle type:")
    print("1. Car")
    print("2. Motorcycle")
    vehicle_type = input("Enter your choice: ")

    if vehicle_type == "1":
        x = Car()
    elif vehicle_type == "2":
        x = Motorcycle()
    else:
        print("Invalid choice, returning to menu.")
        return
    
    x.name = input("Enter vehicle name: ")
    x.fuel = int(input("Enter vehicle fuel: "))
    x.fuel_type = input("Enter vehicle fuel type: ")
    x.speed = int(input("Enter vehicle speed: "))
    Garage.append(x)
    print(f"{x.name} has been added to the garage.")

def view_garage():
    for i in Garage:
        print("-" * 20)
        print(f"{i.name}")
        print(f"Car fuel: {i.fuel}, Fuel type: {i.fuel_type}, Speed: {i.speed}")
    print("-" * 20)

Garage = []

if __name__ == "__main__":
    while True:
        print("1. Create Vehicle")
        print("2. View Garage")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            create_vehicle()
        elif choice == "2":
            view_garage()
        elif choice == "3":
            break
        else:
            print("Invalid choice, please try again.")
