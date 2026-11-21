#https://github.com/Aysel-Ahmadi/Cars-Gallery.git

class Vehicle:

    def __init__(self, model, id, color, price, is_sold):
        self.model = model
        self.id = id
        self.color = color
        self.price = price
        self.is_sold = is_sold

def update_price(self, new_price):
            self.price = new_price

def update_sold_status(self, status):
    self.is_sold = status
   
def sold_text(self):
      if self.is_sold:
        return "Yes"
      else:
        return "No"
class Car(Vehicle):

    def __init__(self, model, id, color, price, is_sold, number_of_doors):
        super().__init__(model, id, color, price, is_sold)
        self.number_of_doors = number_of_doors

    def get_info(self):
        return f"Car | ID: {self.id} | Model: {self.model} | Color: {self.color} | Price: {self.price} | Sold: {self.sold_text()} | Doors: {self.number_of_doors}"


class Motorcycle(Vehicle):

    def __init__(self, model, id, color, price, is_sold, engine_capacity):
        super().__init__(model, id, color, price, is_sold)
        self.engine_capacity = engine_capacity

    def get_info(self):
        return f"Motorcycle | ID: {self.id} | Model: {self.model} | Color: {self.color} | Price: {self.price} | Sold: {self.sold_text()} | Engine Capacity: {self.engine_capacity}"


class Truck(Vehicle):

    def __init__(self, model, id, color, price, is_sold, cargo_capacity):
        super().__init__(model, id, color, price, is_sold)
        self.cargo_capacity = cargo_capacity

    def get_info(self):
        return f"Truck | ID: {self.id} | Model: {self.model} | Color: {self.color} | Price: {self.price} | Sold: {self.sold_text()} | Cargo Capacity: {self.cargo_capacity}"
n = int(input())
vehicles = {}

for i in range(n):
    data = input().split()

    vehicle_type = data[0]
    vehicle_id = int(data[1])
    model = data[2]
    color = data[3]
    price = int(data[4])
    is_sold = data[5] == "True"
    extra = int(data[6])

    if vehicle_type == "Car":
       vehicle = Car(model, vehicle_id, color, price, is_sold, extra)

    elif vehicle_type == "Motorcycle":
         vehicle = Motorcycle(model, vehicle_id, color, price, is_sold, extra)

    elif vehicle_type == "Truck":
         vehicle = Truck(model, vehicle_id, color, price, is_sold, extra)
vehicles[vehicle_id] = vehicle

q = int(input())

for i in range(q):
    command = input().split()

    if command[0] == "INFO":
        vehicle_id = int(command[1])
        print(vehicles[vehicle_id].get_info())

    elif command[0] == "PRICE":
        vehicle_id = int(command[1])
        new_price = int(command[2])
        vehicles[vehicle_id].update_price(new_price)

    elif command[0] == "SOLD":
        vehicle_id = int(command[1])
        status = command[2] == "True"
        vehicles[vehicle_id].update_sold_status(status)

        