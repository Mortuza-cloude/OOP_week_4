from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, driver_name):
        self.driver_name = driver_name

    @abstractmethod
    def calculate_fare(self, distance_km):
        pass

    def start_trip(self, distance_km):
        fare = self.calculate_fare(distance_km)
        print(f"Driver {self.driver_name} - Trip fare: ¥{fare}")


class Car(Vehicle):
    def calculate_fare(self, distance_km):
        return 400 + (distance_km * 100)   # ¥400 base + ¥100/km


class Bike(Vehicle):
    def calculate_fare(self, distance_km):
        return 150 + (distance_km * 50)    # ¥150 base + ¥50/km


def main():
    trips = []

    while True:
        vehicle_type = input("Vehicle type (car/bike, or 'done' to finish): ")
        if vehicle_type == "done":
            break

        driver_name = input("Driver name: ")
        distance_km = int(input("Distance (km): "))

        if vehicle_type == "car":
            trips.append(Car(driver_name))
        elif vehicle_type == "bike":
            trips.append(Bike(driver_name))
        else:
            print("Unknown vehicle type, skipping.")
            continue

        trips[-1]._pending_distance = distance_km

    for trip in trips:
        trip.start_trip(trip._pending_distance)


if __name__ == "__main__":
    main()