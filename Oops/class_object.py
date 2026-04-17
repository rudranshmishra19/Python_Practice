class Car:
    # Constructer (special method to initialize objects)
    def __init__(self,brand,model,year):
        self.brand=brand  # attribute
        self.model=model # attribute
        self.year=year  #attribute
        
#Method (behavior)
    def display_info(self):
      print(f"{self.year} {self.brand} {self.model}")


# Creating objects (instance of the class)
car1=Car("Tesla", "Model s",2023)
car2=Car("Toyota", "Corolla s",2022)

#using methods
car1.display_info()  #output :2023 Tesla Model s 
car2.display_info()  #output :2022 Toyota Corolla


         