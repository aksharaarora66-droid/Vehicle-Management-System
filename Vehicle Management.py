class Vehicle:
    def __init__(self, vehicleID, brand, model, year, color):
        self.vehicleID = vehicleID
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color

    def display_information(self):
         print(f"""Your vehicle_ID is:{self.vehicleID}
                  Brand of your vehicle is:{self.brand}
                  Model of your vehicle is:{self.model}
                  Year in which you have registered your vehicle is:{self.year}
                  Colour of your vehicle is:{self.color}""")
    def calculate_Mileage(self,Total_Miles_Travelled,Total_Gallons_Used):
        self.Total_Miles_Travelled=Total_Miles_Travelled
        self.Total_Gallons_Used=Total_Gallons_Used
        Mileage=self.Total_Miles_Travelled/self.Total_Gallons_Used
        self.Mileage=Mileage
        print("Mileage of your vehicle is: ",self.Mileage)

class MotorVehicle(Vehicle):
    def __init__(self, vehicleID, brand, model, year, color, engineCapacity, fuelType):
        super().__init__(vehicleID, brand, model, year, color) 
        self.engineCapacity = engineCapacity
        self.fuelType = fuelType
    def check_fuel_level(self,current_litres,tank_capacity):
        self.current_litres=current_litres
        self.tank_capacity=tank_capacity
        fuellevel=(current_litres/tank_capacity)*100
        self.fuel_level=fuellevel
        print("fuel_level is: ",self.fuel_level)

class car(MotorVehicle):
    def __init__(self, vehicleID, brand, model, year, color, engineCapacity, fuelType, numDoors, sittingcapacity):
        super().__init__(vehicleID, brand, model, year, color, engineCapacity, fuelType)
        self.numDoors = numDoors
        self.sittingcapacity = sittingcapacity
        print(f"Car Created -> Doors: {self.numDoors}, Seats: {self.sittingcapacity}")

my_car = car("C001", "Tesla", "Model 3", 2024, "White", 0, "Electric", 4, 5)
my_car.display_information()