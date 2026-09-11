class Rider:
    def __init__(self, name, deliveries =0):
        self.name = name
        self.deliveries = deliveries

    def pay(self):
        return self.deliveries *100
class BicycleRider(Rider):
    def pay(self):
        return self.deliveries *100
class MotorbikerRider(Rider):
    def __init__(self, name, deliveries = 0, fuel_cost = 30):
        super().__init__(name,deliveries)
        self.fuel_cost = fuel_cost
    def pay(self):
        gross = self.deliveries *150 
        return gross - (self.deliveries * self.fuel_cost)
def main():
    riders = []
    
    while True:
        rider_type = input("Enter type(bike/moto, or 'done' to finish: )")
        if rider_type == "done":
            break
        name = input("Rider name:")
        deliveries = int(input("Deliveries Complited: "))

        if rider_type == "bike":
            riders.append(BicycleRider(name, deliveries))
        elif rider_type =="moto":
            riders.append(MotorbikerRider(name,deliveries))
        else:
            print("Unknown rider type, skipping.")
            continue
    for r in riders:
        print(f"{r.name} earned ¥{r.pay()}")
if __name__ =="__main":
    main()
