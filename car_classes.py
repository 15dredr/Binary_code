class Car:
    def __init__(self, make, model, year, colour, condition, price, location):
        self.make = make
        self.model = model
        self.year = year
        self.colour = colour
        self.condition = condition
        self.price = price
        self.location = location

    def display(self):
        print("Make: " + self.make)
        print("Model: " + self.model)
        print("Year: " + self.year)
        print("Colour: " + self.colour)
        print("Condition: " + self.condition)
        print("Price: " + self.price)
        if self.location == "SOLD":
            print("This car is sold")
        else:
            print("Location: " + self.location)

    def on_sale(self):
        price = float(self.price)
        price = price * 0.8
        self.price = str(price)
        print("This car is on sale for £" + self.price)
        return self.price

    def sale_over(self):
        price = float(self.price)
        self.price = price * 1.25
        return self.price

    def move_location(self, new_lot):
        self.location = new_lot
        return self.location

    def sold(self):
        self.price = "None"
        self.location = "SOLD"
        return self.price and self.location


my_car = Car("BMW", "Active Tourer", "2019", "Blue", "Good", "15000", "Lot 2")
my_car.display()
my_car.on_sale()
my_car.sale_over()
print(my_car.price)
my_car.sold()
my_car.display()

