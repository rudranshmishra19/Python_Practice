#creating a class engine which will an attribute of car 
class Engine:
    def __init__(self,horsepower):
           self.__horsepower=horsepower #private access
    def get_horsepower(self):   #getter method to access horsepoweer
         return self.__horsepower     
    # in case we need to change the value of horsepower  
    def set_horsepower(self,new_horsepower):
         self.__horsepower= new_horsepower
#creating a car class           
class car:
      def __init__(self,make,model,color,engine):  #passing parameter for attribute to constructor
            self.make=make  
            self.model=model
            self.color=color
            self._engine=engine   #Engine object is now an attribute of car
            # define a method 
      def define(self):
            print(f"car make is  {self.make}, model is {self.model}, color is {self.color}"
                     f" and engine horsepower is {self._engine.get_horsepower()} ")   
      @staticmethod #define a static method which is not bound either to class or object
      def add(a,b):
       return a+b  
#creating an object      
my_engine=Engine(400)       
my_car=car("BMW","1F2G","Brownish-red",my_engine)
result=car.add(446,64)
print(result)
#changing the value of horsepower
my_engine.set_horsepower(699)
my_car.define()