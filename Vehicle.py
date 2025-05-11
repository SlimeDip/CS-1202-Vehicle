from abc import ABC, abstractmethod
import time
import os

class Vehicle(ABC):
    def __init__(self):
        self._name = None
        self._speed = 0
        self._fuel = 0
        self._max_fuel = 0
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
        if value <= 0:
            self._speed = 60
            print("Speed cannot be negative, setting to default value of 60 km/h.")
        else:
            self._speed = value

    @property
    def fuel(self):
        return self._fuel
    
    @fuel.setter
    def fuel(self, value):
        if value < 0:
            self._fuel = 60
            print("Fuel cannot be negative, setting to default value of 60L.")
        else:
            self._fuel = value

    @property
    def max_fuel(self):
        return self._max_fuel
    
    @max_fuel.setter
    def max_fuel(self, value):
        if value < 0:
            self._max_fuel = 60
            print("Max fuel cannot be negative, setting to default value of 60L.")
        else:
            self._max_fuel = value

    @property
    def fuel_type(self):
        return self._fuel_type
    
    @fuel_type.setter
    def fuel_type(self, value):
        if value.lower() not in ["gasoline", "diesel", "electric"]:
            self._fuel_type = "Gasoline"
            print("Invalid fuel type, setting to default value of Gasoline.")
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

class LandVehicle(Vehicle):
    def __init__(self):
        super().__init__()
        self._terrain = "land"

class WaterVehicle(Vehicle):
    def __init__(self):
        super().__init__()
        self._terrain = "water"

    @property
    def speed(self):
        return self._speed * 0.539957

    @speed.setter
    def speed(self, value):
        if value <= 0:
            self._speed = 60 / 0.539957
            print("Speed cannot be negative, setting to default value of 60 knots")
        else:
            self._speed = value

class Car(LandVehicle):
    def start_engine(self):
        print("Car engine started")

    def stop_engine(self):
        print("Car engine stopped")

    def drive(self, amount):
        if self.fuel <= 0:
            print("Cannot drive, fuel is empty")
            return
        self.fuel -= amount

    def refuel(self):
        self.fuel = self.max_fuel
        print(f"Car refueled: {self.fuel}L / {self.max_fuel}L")

class Motorcycle(LandVehicle):
    def start_engine(self):
        print("Motorcycle engine started")

    def stop_engine(self):
        print("Motorcycle engine stopped")

    def drive(self, amount):
        if self.fuel <= 0:
            print("Cannot drive, fuel is empty")
            return
        self.fuel -= amount

    def refuel(self):
        self.fuel = self.max_fuel
        print(f"Motorcycle refueled: {self.fuel}L / {self.max_fuel}L")

class Bus(LandVehicle):
    def start_engine(self):
        print("Bus engine started")

    def stop_engine(self):
        print("Bus engine stopped")

    def drive(self, amount):
        if self.fuel <= 0:
            print("Cannot drive, fuel is empty")
            return
        self.fuel -= amount

    def refuel(self):
        self.fuel = self.max_fuel
        print(f"Bus refueled: {self.fuel}L / {self.max_fuel}L")

class Truck(LandVehicle):
    def start_engine(self):
        print("Truck engine started")

    def stop_engine(self):
        print("Truck engine stopped")

    def drive(self, amount):
        if self.fuel <= 0:
            print("Cannot drive, fuel is empty")
            return
        self.fuel -= amount

    def refuel(self):
        self.fuel = self.max_fuel
        print(f"Truck refueled: {self.fuel}L / {self.max_fuel}L")

class Speedboat(WaterVehicle):
    def start_engine(self):
        print("Speedboat engine started")

    def stop_engine(self):
        print("Speedboat engine stopped")

    def drive(self, amount):
        if self.fuel <= 0:
            print("Cannot drive, fuel is empty")
            return
        self.fuel -= amount

    def refuel(self):
        self.fuel = self.max_fuel
        print(f"Speedboat refueled: {self.fuel}L / {self.max_fuel}L")

class Jetski(WaterVehicle):
    def start_engine(self):
        print("Jetski engine started")

    def stop_engine(self):
        print("Jetski engine stopped")

    def drive(self, amount):
        if self.fuel <= 0:
            print("Cannot drive, fuel is empty")
            return
        self.fuel -= amount

    def refuel(self):
        self.fuel = self.max_fuel
        print(f"Jetski refueled: {self.fuel}L / {self.max_fuel}L")

def create_vehicle():
    print("Select vehicle type:")
    print("1. Car")
    print("2. Motorcycle")
    print("3. Bus")
    print("4. Truck")
    print("5. Speedboat")
    print("6. Jetski")
    vehicle_type = input("Enter your choice: ")

    if vehicle_type == "1":
        x = Car()
    elif vehicle_type == "2":
        x = Motorcycle()
    elif vehicle_type == "3":
        x = Bus()
    elif vehicle_type == "4":
        x = Truck()
    elif vehicle_type == "5":
        x = Speedboat()
    elif vehicle_type == "6":
        x = Jetski()
    else:
        print("Invalid choice, returning to menu.")
        time.sleep(1)
        clear()
        return
    
    try:
        x.name = input("Enter vehicle name: ")
        max_fuel = int(input("Enter vehicle fuel capacity (Liter): "))
        x.max_fuel = max_fuel if max_fuel > 0 else -1
        x.fuel = x.max_fuel
        x.fuel_type = input("Enter vehicle fuel type (Gasoline, Diesel, Electric): ")
        if isinstance(x, LandVehicle):
            x.speed = int(input("Enter vehicle speed (km/h): "))
            Garage.append(x)
            print(f"\n{x.name} has been added to the garage.")
        elif isinstance(x, WaterVehicle):
            x.speed = int(input("Enter vehicle speed (knots): ")) / 0.539957
            Dock.append(x)
            print(f"\n{x.name} has been added to the dock.")
    except ValueError:
        print("Invalid input, please enter numeric values for fuel and speed.")
        time.sleep(1)

def view_garage():
    global CurrentVehicle

    print("-" * 20)
    print(" G A R A G E")
    for j, i in enumerate(Garage):
        print("-" * 20)
        print(f"{j+1}. {i.name}")
        print(f"Vehicle type: {type(i).__name__}")
        print(f"Vehicle fuel: {i.fuel} L | Fuel type: {i.fuel_type} | Speed: {i.speed} km/h")
    print("-" * 20)

    try:
        choice = int(input("\nSelect vehicle to drive: "))
        if choice < 1 or choice > len(Garage):
            print("Invalid choice.")
            time.sleep(1)
            clear()
            return
        CurrentVehicle = Garage[choice - 1]
    except ValueError:
        print("Invalid input, please enter a number.")
        time.sleep(1)

def view_dock():
    global CurrentVehicle

    print("-" * 20)
    print(" D O C K")
    for j, i in enumerate(Dock):
        print("-" * 20)
        print(f"{j+1}. {i.name}")
        print(f"Vehicle type: {type(i).__name__}")
        print(f"Vehicle fuel: {i.fuel} L | Fuel type: {i.fuel_type} | Speed: {i.speed:.2f} kn")
    print("-" * 20)

    try:
        choice = int(input("\nSelect vehicle to drive: "))
        if choice < 1 or choice > len(Dock):
            print("Invalid choice.")
            time.sleep(1)
            clear()
            return
        CurrentVehicle = Dock[choice - 1]
    except ValueError:
        print("Invalid input, please enter a number.")
        time.sleep(1)

def drive_sim(CurrentVehicle):
    while True:
        unit = "kn" if CurrentVehicle._terrain == "water" else "km/h"
        print(f"Current vehicle: {CurrentVehicle.name}")
        print(f"Fuel: {round(CurrentVehicle.fuel, 2)}L / {round(CurrentVehicle.max_fuel, 2)}L | Speed: {CurrentVehicle.speed:.2f} {unit}\n")
        print("Select an action:")
        print("1. Drive")
        print("2. Refuel")
        print("3. Stop Engine")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            label = "nautical miles" if CurrentVehicle._terrain == "water" else "km"
            clear()

            distance = float(input(f"Enter distance to drive (in {label}): "))
            if distance <= 0:
                print("Distance must be greater than 0.")
                time.sleep(1)
                clear()
                continue
            if distance > CurrentVehicle.fuel:
                print("Not enough fuel to drive this distance.")
                time.sleep(1)
                clear()
                continue

            CurrentVehicle.fuel -= distance

            print(f"Driving {distance} {label}")
            print("Driving", end=" ", flush=True)
            for _ in range(3):
                print(".", end=" ", flush=True)
                time.sleep(1)
            print(f"\nYou traveled {distance} {label} in {distance / round(CurrentVehicle.speed, 2):.2f} hours.")
            print(f"\nArrived at destination!")
            time.sleep(3)
        elif choice == "2":
            clear()
            print("Refueling", end=" ", flush=True)
            for _ in range(3):
                print(".", end=" ", flush=True)
                time.sleep(1)
            print("\n", end="")
            CurrentVehicle.refuel()
            CurrentVehicle.fuel = round(CurrentVehicle.fuel, 2)
            time.sleep(1)
        elif choice == "3":
            clear()
            CurrentVehicle.stop_engine()
            time.sleep(1)
            break
        else:
            print("Invalid choice, please try again.")
            time.sleep(1)
        clear()

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

Garage = []
Dock = []

car = Car()
car.name = "Family Car"
car.fuel = 50
car.max_fuel = 50
car.fuel_type = "Gasoline"
car.speed = 120
Garage.append(car)

motorcycle = Motorcycle()
motorcycle.name = "Sport Bike"
motorcycle.fuel = 15
motorcycle.max_fuel = 15
motorcycle.fuel_type = "Gasoline"
motorcycle.speed = 180
Garage.append(motorcycle)

bus = Bus()
bus.name = "City Bus"
bus.fuel = 200
bus.max_fuel = 200
bus.fuel_type = "Diesel"
bus.speed = 80
Garage.append(bus)

truck = Truck()
truck.name = "Freight Truck"
truck.fuel = 300
truck.max_fuel = 300
truck.fuel_type = "Diesel"
truck.speed = 100
Garage.append(truck)

boat = Speedboat()
boat.name = "Speedy"
boat.fuel = 100
boat.max_fuel = 100
boat.fuel_type = "Gasoline"
boat.speed = 40 / 0.539957
Dock.append(boat)

jetski = Jetski()
jetski.name = "Wave Rider"
jetski.fuel = 50
jetski.max_fuel = 50
jetski.fuel_type = "Gasoline"
jetski.speed = 60 / 0.539957
Dock.append(jetski)

CurrentVehicle = Garage[0]

if __name__ == "__main__":
    clear()
    while True:
        print(f"Current vehicle: {CurrentVehicle.name}\n")
        print("Select an option:")
        print("1. Create Vehicle")
        print("2. View Garage")
        print("3. View Dock")
        print("4. Drive Vehicle")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            clear()
            create_vehicle()
            time.sleep(1)
        elif choice == "2":
            clear()
            view_garage()
        elif choice == "3":
            clear()
            view_dock()
        elif choice == "4":
            clear()
            print("Starting engine", end=" ", flush=True)
            for _ in range(3):
                print(".", end=" ", flush=True)
                time.sleep(1)
            print("\n", end="")
            CurrentVehicle.start_engine()
            print()
            time.sleep(1)
            clear()
            drive_sim(CurrentVehicle)
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice, please try again.")
            time.sleep(1)
        clear()
