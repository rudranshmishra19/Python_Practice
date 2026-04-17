class Car:
    def __init__(self,fuel):
        self.acc=False
        self.brk=False
        self.cluth=False
        # Liters of fuel 
        self.fuel=fuel

    def start(self):
        if self.fuel >0:
            self.cluth=True
            self.acc=True
            print("Car started .....")
        else:
            print("Cannot start! no fuel")

    def stop(self):
        self.acc=False
        print("Car Stopped ")            

car1=Car(fuel=5)
car1.start()
car1.stop()

car2=Car(fuel=0)
car2.start()

