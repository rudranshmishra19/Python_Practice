class Student:
    # constructor ivoking 
    # Default constructor
    # Defining class attribute\
    college_name="Union College"
    name="Anonoymous"
    def __init__(self):
        print("Adding new student in Database ...")
        
    # Parametrized constructor
    def __init__(self,name,age,marks):
        # Object attribute
        self.name=name  # Obj att> class attr
        self.age=age
        self.marks=marks
        
    def display(self):
         print(f"Name :{self.name},Age :{self.age} , Makrs:{self.marks}, Collge: {self.college_name}")   

    def welcome(self):
        print("Welcome student")


# Create a list to store all students
students=[]
# Add Student objects into the list
students.append(Student("Rudransh",25,99))  
students.append(Student("Jeet",24,54))  
students.append(Student("Meet",26,78))  
students.append(Student("Suresh",26,89))  
students.append(Student("Gayatri",21,89))  


# Displaying database f

print("\n ----Student Database ----")
for student in students:
    student.display()

