#creating a class laptop
class laptop:
    name="Dell"
    model=""
    screen_size=14
    battery="45w"
    def description(self):  # creating method 
         print(f"laptop:{self.name} \nModel:{self.model}\nscreen {self.screen_size}\nbattery {self.battery}")
    def clone(self):
         new_laptop=laptop()
         new_laptop.name=self.name
         new_laptop.model=self.model
         new_laptop.screen_size=self.screen_size
         new_laptop.battery=self.battery
         return new_laptop
#create an object
my_laptop=laptop()
my_laptop.name    
my_laptop.model="X415EA"
my_laptop.screen_size
my_laptop.battery
my_laptop.description()
print(" ")
# creating another instance  from an instance
another_lapop= my_laptop.clone()
another_lapop.description()
