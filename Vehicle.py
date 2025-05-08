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
        if value not in ["gasoline", "diesel", "electric"]:
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

if __name__ == "__main__":
    Car1 = Car()
    Car1.name = "Honda Civic"
    Car1.fuel = 50
    Car1.fuel_type = "gasoline"
    Car1.speed = 60

    Car2 = Car()
    Car2.name = "Toyota Innova"
    Car2.fuel = 30
    Car2.fuel_type = "diesel"
    Car2.speed = 80

    Garage = [Car1, Car2]

    for car in Garage:
        print("-" * 20)
        print(f"{car.name}")
        print(f"Car fuel: {car.fuel}, Fuel type: {car.fuel_type}, Speed: {car.speed}")
    
    print("-" * 20)