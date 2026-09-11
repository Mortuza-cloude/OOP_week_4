class DineInOrder:
    def __init__(self, table, items):
        self.table = table
        self.items = items

    def print_ticket(self):
        print(f"[DINE-IN] Table {self.table}: {', '.join(self.items)}")


class TakeoutOrder:
    def __init__(self, number, items):
        self.number = number
        self.items = items

    def print_ticket(self):
        print(f"[TAKEOUT] #{self.number}: {', '.join(self.items)}")


class DeliveryOrder:
    def __init__(self, address, items):
        self.address = address
        self.items = items

    def print_ticket(self):
        print(f"[DELIVERY] {self.address}: {', '.join(self.items)}")


def main():
    orders = []

    while True:
        order_type = input("Order type (dinein/takeout/delivery, or 'done' to finish): ")
        if order_type == "done":
            break

        if order_type == "dinein":
            table = input("Table number: ")
            items_raw = input("Items (comma-separated): ")
            items = [i.strip() for i in items_raw.split(",")]
            orders.append(DineInOrder(table, items))

        elif order_type == "takeout":
            number = input("Order number: ")
            items_raw = input("Items (comma-separated): ")
            items = [i.strip() for i in items_raw.split(",")]
            orders.append(TakeoutOrder(number, items))

        elif order_type == "delivery":
            address = input("Delivery address: ")
            items_raw = input("Items (comma-separated): ")
            items = [i.strip() for i in items_raw.split(",")]
            orders.append(DeliveryOrder(address, items))

        else:
            print("Unknown order type, skipping.")
            continue

    for order in orders:
        order.print_ticket()


if __name__ == "__main__":
    main()

