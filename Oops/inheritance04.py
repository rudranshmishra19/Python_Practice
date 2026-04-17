class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    
    def work(self):
        print(f"{self.name} is working")

class Developer(Employee):  #inherit from employeee
    def __init__(self, name, salary,language):
        super().__init__(name, salary)
        self.language=language

    def code(self):
        print(f"{self.name} is coding in {self.language}")

dev=Developer("Rudransh",10000,"python")
dev.work()
dev.code()
