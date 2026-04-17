#creating a class as school
class School:
    School_name="MRMV KUMKUM ENGLISH SCHOOL"
    def __init__(self,name,roll_no):  #constructing instance attribute 
          self.name=name
          self.roll_no=roll_no
    def greet(self): #method for object attribute
         print(f"Hii my name is {self.name} ,Rollno:{self.roll_no},School:{self.School_name}")     
    @classmethod #method for class attribute
    def change_school(cls,new_school):
        cls.School_name=new_school #update the class attribute
    @staticmethod #static method
    def school_motto():
         return "Make money by educating students"   
        
#creating an object

rudransh=School("Rudransh",24)
print((School.school_motto()))
School.change_school("Omkar International School") #change the name of school
rudransh.greet()
#creating 2nd instance
omkar=School("Omkar",33) 
#change school name
School.change_school("Don Bosco High School")
# calling instance attribute
omkar.greet()  
