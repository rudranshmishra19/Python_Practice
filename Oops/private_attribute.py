# class person:
#     def __init__(self,name,age):
#         self.name=name      #public attribute
#         self.__age=age       #private attribute

#     def display(self):
#         print(f"Name:{self.name}, Age:{self.__age}")

# p=person("Alice",25)
# p.display()

# #Accessing attributes
# print(p.name)    #works (publie)
# #print age

# Access private Attribute via Getter/Setter

class BankAccount:
    def __init__(self,balance):
        self.__balance=balance #private attribute

    #Getter
    def get_balance(self):
        return self.__balance
    #Setter
    def deposit(self,amount):
        if amount > 0:
            self.__balance+=amount
        else:
            print("Invalid deposit amount ")       

    def withdraw(self,amount):
        if 0 <amount<=self.__balance:
            self.__balance-=amount
        else:
            print("Insufficient balance or invalid amount")

#Usage
acc=BankAccount(1000)
print("Balance:",acc.get_balance())


    