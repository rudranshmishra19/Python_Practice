class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display_info(self):
        return f"{self.name} {self.age}"
         
class student(person):
    def __init__(self, id,std, name, age):
        # call parent __init__
        super().__init__(name,age)
        self.id=id
        self.std=std

    def display_info(self):
        return f"{self.name} {self.age} {self.id} {self.std}"


s1=student("X123","X","Rudransh",23)
print(s1.display_info())
    




