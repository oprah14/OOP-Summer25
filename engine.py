cars = {
    "Car1": {"brand": "Toyota", "model": "Corolla", "year": 2020, "type": "Sedan", "color": "Red"},
    "Car2": {"brand": "Honda", "model": "Civic", "year": 2021, "type": "Sedan", "color": "Blue"},
    "Car3": {"brand": "Ford", "model": "Mustang", "year": 2022, "type": "Coupe", "color": "Black"}
}


for car, attributes in cars.items():
    print(f"{car}: {attributes}")


cars["Car1"]["color"] = "Green"  

class Car:
    def __init__(self, brand, model, year, car_type, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.type = car_type
        self.color = color


    def display_info(self):
        return f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}, Type: {self.type}, Color: {self.color}"

    def update_color(self, new_color):
        self.color = new_color


car1 = Car("Toyota", "Corolla", 2020, "Sedan", "Red")
car2 = Car("Honda", "Civic", 2021, "Sedan", "Blue")
car3 = Car("Ford", "Mustang", 2022, "Coupe", "Black")


print(car1.display_info())
print(car2.display_info())
print(car3.display_info())


car1.update_color("Green")


class Engine:
    def __init__(self, engine_type, capacity, horsepower, fuel_type, cylinders):
        self.engine_type = engine_type
        self.capacity = capacity
        self.horsepower = horsepower
        self.fuel_type = fuel_type
        self.cylinders = cylinders


    def display_engine_info(self):
        return (f"Engine Type: {self.engine_type}, Capacity: {self.capacity}, "
                f"Horsepower: {self.horsepower} HP, Fuel Type: {self.fuel_type}, "
                f"Cylinders: {self.cylinders}")


class Car:
    def __init__(self, brand, model, year, car_type, color, engine):
        self.brand = brand
        self.model = model
        self.year = year
        self.type = car_type
        self.color = color
        self.engine = engine

   
    def display_car_info(self):
        return (f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}, "
                f"Type: {self.type}, Color: {self.color}, Engine: {self.engine.display_engine_info()}")

engine1 = Engine("Combustion", "2.0L", 250, "Petrol", 4)
engine2 = Engine("Electric", "0L", 200, "Electric", 0)
engine3 = Engine("Hybrid", "1.5L", 180, "Hybrid", 4)


car1 = Car("Toyota", "Corolla", 2020, "Sedan", "Red", engine1)
car2 = Car("Honda", "Civic", 2021, "Sedan", "Blue", engine2)
car3 = Car("Ford", "Mustang", 2022, "Coupe", "Black", engine3)


print(car1.display_car_info())
print(car2.display_car_info())
print(car3.display_car_info())