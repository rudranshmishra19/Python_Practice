#Defining a class
class person:
    def __init__(self,name,age):
        self.name=name  #Attribute
        self.age=age    #Attribute
    
    def greet(self):
          print(f"Hello! my name is {self.name} my age is {self.age}")


#creating an object

person1=person("Rudransh",22)
person2=person("Omkar",21)
person3=person("jeet",22)
#Accessing attributes and method

print(person1.name,person2.name,person3.name)  #output :Alice
person1.greet()
person2.greet()
person3.greet()
 
    

