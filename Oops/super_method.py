class Bike:
    def __init__(self,name,engine):
        self.name=name
        self.engine=engine

    @staticmethod
    def start():
        print("Bike started...")

    @staticmethod
    def gear():
        print(" Cluth pressed switched to gear one")

    @staticmethod
    def race():
        print("Clutch Released and Bike is now running")    

    @staticmethod
    def stop():
        print(" Down break applied bike stopped...")
    
    #print Common attributes
    def display_common(self):
        print(f"Name:{self.name},Engine:{self.engine}")


class HeroBike(Bike):
    def __init__(self,name,engine,brake):
        super().__init__(name,engine)
        self.brake=brake

    #Method to print all attributes
    def display(self):
        self.display_common()
        print(f"Brake:{self.brake}")
    @staticmethod 
    def race():
        print("HeroBike is now racing....")


class RoyalEnfield(Bike):
    def __init__(self, name, engine,front_brake,rear_brake):
        super().__init__(name, engine)
        self.front_brake=front_brake
        self.rear_brake=rear_brake

    def display(self):
        self.display_common()
        print(f"Front Brake:{self.front_brake},Rear Brake:{self.rear_brake}")


hb1=HeroBike("Hero Splendor","97.2cc","Disc")
Ry1=RoyalEnfield("Ry350","349cc","Disc","Drum_Brakes")

#print all details 
hb1.display()
hb1.start(),hb1.gear(),hb1.race(),hb1.stop()
print()
Ry1.display()