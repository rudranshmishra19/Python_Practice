class Employee:
    def role(self):
        print("I am an employee")
    
class Developer(Employee):
    def role(self):
        print("I am a Developer")

class Manager(Employee):
    def role(self):
        print("I am a manager")

employees=[Employee(),Developer(),Manager()]

for emp in employees:
    emp.role()   #har ke apna alag role print kargea 

    

