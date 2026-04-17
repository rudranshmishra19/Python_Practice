class student:
    def __init__(self,name,age,sex,fees):
        self.name=name
        self.age=age
        self.sex=sex
        self.__fees=fees

    def get_fees(self):
        return self.__fees
    
    def set_fees(self,fees_amount):
        if fees_amount >0:
            self.__fees=fees_amount

s1=student("Rudransh",23,"male",100000)
print(s1.get_fees())
s1.set_fees(200000)
print(s1.get_fees())
print(s1.name)
print(s1.age)
print(s1.sex)







        