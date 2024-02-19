class Vehicle:
    def __init__(self, marca , modelo , año): 
        self.marca = marca
        self.modelo = modelo 
        self.año = año 
    

class Car(Vehicle): 
    pass 
class Bike(Vehicle): 
    pass
class Boat(Vehicle): 
    pass 
class Plane(Vehicle): 
    pass

carro1 = Car("Toyota", "Sequoia", 2024)
carro2 = Car("Mercedes-Benz", "GLC300", 2023)

moto1= Bike("BMW", "S 1000 XR", 2023)
moto2 = Bike("Bera", "Gbr 200", 2024)

avion1= Plane("Embraer" ,"Preator 500/600", 2018)
avion2 = Plane ("Pilatus Aeronave", "Pilatus PC-24", 2013)

barco1= Boat("Lagoon", "Lagoon 51", 2022)
barco2 = Boat("Jeanneau", "Jeanneau 60 YACHT", 2024)

print(carro2.marca)