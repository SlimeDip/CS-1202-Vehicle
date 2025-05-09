from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self):
        self._name = None
        self._speed = 0
        self._fuel = 0
        self._maxfuel = 0
        self._fuel_type = None

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
            self._speed = 60
            print("Speed cannot be negative, setting to default value of 60 km/h")
        else:
            self._speed = value

    @property
    def fuel(self):
        return self._fuel
    
    @fuel.setter
    def fuel(self, value):
        if value < 0:
            self._fuel = 60
            print("Fuel cannot be negative, setting to default value of 60L")
        else:
            self._fuel = value

    @property
    def max_fuel(self):
        return self._maxfuel
    
    @max_fuel.setter
    def max_fuel(self, value):
        if value < 0:
            self._maxfuel = 60
            print("Max fuel cannot be negative, setting to default value of 60L")
        self._maxfuel = value

    @property
    def fuel_type(self):
        return self._fuel_type
    
    @fuel_type.setter
    def fuel_type(self, value):
        if value.lower() not in ["gasoline", "diesel", "electric"]:
            self._fuel_type = "Gasoline"
            print("Invalid fuel type, setting to default value of Gasoline")
        else:
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

    def refuel(self):
        self._fuel = self.max_fuel
        print(f"Car refueled: {self._fuel}/{self.max_fuel}")

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

    def refuel(self):
        self._fuel = self.max_fuel
        print(f"Motorcycle refueled: {self._fuel}/{self.max_fuel}")

class Bus(Vehicle):
    def start_engine(self):
        print("Bus engine started")

    def stop_engine(self):
        print("Bus engine stopped")

    def drive(self, amount):
        if self._fuel <= 0:
            print("Cannot drive, fuel is empty")
            return
        self._fuel -= amount

    def refuel(self):
        self._fuel = self.max_fuel
        print(f"Bus refueled: {self._fuel}/{self.max_fuel}")

def create_vehicle():
    print("Select vehicle type:")
    print("1. Car")
    print("2. Motorcycle")
    print("3. Bus")
    vehicle_type = input("Enter your choice: ")

    if vehicle_type == "1":
        x = Car()
    elif vehicle_type == "2":
        x = Motorcycle()
    elif vehicle_type == "3":
        x = Bus()
    else:
        print("Invalid choice, returning to menu.")
        return
    
    try:
        x.name = input("Enter vehicle name: ")
        x.max_fuel = int(input("Enter vehicle fuel capacity (Liter): "))
        x.fuel = x.max_fuel
        x.fuel_type = input("Enter vehicle fuel type (Gasoline, Diesel, Electric): ")
        x.speed = int(input("Enter vehicle speed (km/h): "))
        Garage.append(x)
        print(f"{x.name} has been added to the garage.")
    except ValueError:
        print("Invalid input, please enter numeric values for fuel and speed.")

def view_garage():
    global CurrentVehicle
    
    for j, i in enumerate(Garage):
        print("-" * 20)
        print(f"{j+1}. {i.name}")
        print(f"Vehicle type: {type(i).__name__}")
        print(f"Vehicle fuel: {i.fuel}L, Fuel type: {i.fuel_type}, Speed: {i.speed}km/h")
    print("-" * 20)

    choice = int(input("Select vehicle to drive (1, 2, ...): "))
    if choice < 1 or choice > len(Garage):
        print("Invalid choice.")
        return
    CurrentVehicle = Garage[choice - 1]

def drive_sim():
    global CurrentVehicle
    while True:
        print(f"Current vehicle: {CurrentVehicle.name}")
        print(f"Fuel: {CurrentVehicle.fuel}L/{CurrentVehicle.max_fuel}L, Speed: {CurrentVehicle.speed}km/h")
        print("Select an action:")
        print("1. Drive")
        print("2. Refuel")
        print("3. Stop Engine")
        choice = input("Enter your choice: ")
        print()
        
        if choice == "1":
            distance = int(input("Enter distance to drive: "))
            if distance > CurrentVehicle.fuel:
                print("Not enough fuel to drive this distance.")
                continue
            CurrentVehicle.fuel -= distance
        elif choice == "2":
            CurrentVehicle.refuel()
        elif choice == "3":
            CurrentVehicle.stop_engine()
            break
        else:
            print("Invalid choice, please try again.")
        print()

x = Car()
x.name = "Default Car"
x.fuel = 50
x.max_fuel = 50
x.fuel_type = "Gasoline"
x.speed = 120

Garage = [x]
CurrentVehicle = Garage[0]

if __name__ == "__main__":
    while True:
        print(f"Current vehicle: {CurrentVehicle.name}")
        print("Select an option:")
        print("1. Create Vehicle")
        print("2. View Garage")
        print("3. Drive Vehicle")
        print("4. Exit")
        choice = input("Enter your choice: ")
        print()
        
        if choice == "1":
            create_vehicle()
        elif choice == "2":
            view_garage()
        elif choice == "3":
            CurrentVehicle.start_engine()
            drive_sim()
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice, please try again.")

        print()
