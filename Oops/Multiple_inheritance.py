# School name declared 
class school:
    @staticmethod
    def school_name():
        return "Omkar international school"

# Defining person 
class person:
    def __init__(self,name,age):
         self.name=name
         self.age=age
    # Function to return the information on person 
    def person_info(self):
        return f"Name:{self.name},Age:{self.age}"

#mutiple Inheritance 
class Student(school,person):
    def __init__(self, name, age,student_id):
        #call person's constructor
        person.__init__(self,name,age)
        self.student_id=student_id

    def student_info(self):
     return f"ID :{self.student_id}, {self.person_info()},School:{self.school_name()}"

#Creating student object 
s1=Student("Rudransh", 23, "S101")

# Printing details 
print(s1.student_info())
  
   