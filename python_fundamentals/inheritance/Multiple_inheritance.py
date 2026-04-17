class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def define(self):
        print(f"Name :{self.name}, Age{self.age}")

class employee:
    def __init__(self,empid,level,salary):
        self.empid=empid
        self.level=level
        self.salary=salary
    

    def display(self):
        print(f"Empid :{self.empid},Level:{self.level},Salary {self.salary}")

class manager(person,employee):
    def __init__(self, name, age,empid,level,salary,department):
        person.__init__(self,name,age)
        employee.__init__(self,empid,level,salary)
        self.department=department

    def display_manager(self):
           self.define()
           self.display()
           print(f"Department:{self.department}")

#creat an object
Manager=manager("Rudransh",22,620710,3,200000,"IT")
Manager.display_manager()             