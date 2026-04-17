#creating a class as school
class School:
    std="10th"
    def __init__(self,name,roll_no):  #constructing instance attribute 
          self.name=name
          self.roll_no=roll_no
    def greet(self): #method for object attribute
         print(f"Hii my name is {self.name} ,Rollno:{self.roll_no},std:{self.std}")     
    @classmethod #method for class attribute
    def change_std(cls,new_std):
        cls.std=new_std #update the class attribute
#creating an object
rudransh=School("Rudransh",24)
#change the std using class method
School.change_std("5th")
rudransh.greet()    
