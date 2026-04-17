class Vechicle:
    def __init__(self,brand,year):
        self.brand=brand
        self.year=year


    def display_info(self):
        print(f"{self.year} {self.brand}")

#Child class(inherits from Vechicle )
class Car(Vechicle):
    def __init__(self, brand, year,model):
        # call parent class constructer
        super().__init__(brand, year)
        self.model= model


        #Overriding method
        def display_info(self):
            print(f"{self.year} {self.brand} {self.model}")

#child class (inherits from Vechicle)
class Bike(Vechicle):
    def __init__(self, brand, year,type):
        super().__init__(brand, year)
        self.type=type

    def display_info(self):
        print(f"{self.year} {self.brand} ({self.type} bike)")

#Create objects
car1=Car("Tesla", 2023, "Model s")
bike1=Bike("Yamaha", 2021, "Sport")


#Use methods
car1.display_info()
bike1.display_info()



