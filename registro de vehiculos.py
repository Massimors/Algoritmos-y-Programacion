class carro: 
    def _init_(self, marca, modelo, año,): 
        self.marca = marca
        self.modelo = modelo
        self.año = año 

class motos: 
    def _init_(self, marca, modelo, año): 
        self.marca = marca
        self.modelo = modelo
        self.año = año

class aviones: 
    def _init_(self, marca, modelo, año): 
        self.marca = marca
        self.modelo = modelo
        self.año = año

class barcos: 
    def _init_(self, marca, modelo, año): 
        self.marca = marca
        self.modelo = modelo
        self.año = año



carro1 =carro("Toyota", "Sequoia", 2024)
carro2 = carro("Mercedes-Benz", "GLC300", 2023)

moto1= motos("BMW", "S 1000 XR", 2023)
moto2 = motos("Bera", "Gbr 200", 2024)

avion1= aviones("Embraer" ,"Preator 500/600", 2018)
avion2 = aviones ("Pilatus Aeronave", "Pilatus PC-24", 2013)

barco1= barcos("Lagoon", "Lagoon 51", 2022)
barco2 = barcos("Jeanneau", "Jeanneau 60 YACHT", 2024)


print (avion1.modelo)