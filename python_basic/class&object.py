# class Person:
#     def __init__(self, name, age):
#         self.name=name
#         self.age=age

#     def __str__(self):
#         return f"{self.name} is {self.age} years old"

# person=Person("Alice",25)
# print(person)

class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def __str__(self):
        return f"{self.brand} {self.model}"

car=Car("Toyota","Camry")
print(car)
        
        

        