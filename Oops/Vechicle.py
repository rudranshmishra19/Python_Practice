# class Vechice:
#     def fuel_type(self):
#         print("Vechile can run on different types of fuel")

# class Car(Vechice):
#     def fuel_type(self):
#         print("Cars run on patrol or Disel")

# class ElectricCar(Vechice):
#     def fuel_type(self):
#         print("Cars runs on battery")

# v=Vechice()
# c=Car()
# e=ElectricCar()

# v.fuel_type()
# c.fuel_type()
# e.fuel_type()

class Employee:
    def salary(self):
        return 3000
    
class Developer(Employee):
    def salary(self):
        return 60000 

class Manager(Employee):
    def salary(self):
        return 80000

emp=Employee()
dev=Developer()
mgr=Manager()

print("Employee Salary",emp.salary())
print("Developer Salary",dev.salary())
print("Manager Salary",mgr.salary())
