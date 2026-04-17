class Employee:
    # Declare a company name 
    Company_name="Albeck Industy"

    def __init__(self,name, age):
        #instane variable (unique to each other)
        self.name=name
        self.age=age

    def display(self):
        #print both employee name and company name
        print(f"Employee Name:{self.name} ,Age:{self.age} ,Company Name: {Employee.Company_name}")    

#Creating objects
E1=Employee("Rudransh", 22)
E2=Employee("Meet",22)

print(E1.Company_name)
E1.display()
E2.display()
