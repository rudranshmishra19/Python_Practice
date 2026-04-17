class BankAccount:
    def __init__(self,balance):
        self.__balance=balance #private attribute

    #Getter
    def get_balance(self):
        return self.__balance

    #setter
    def deposit(self,amount):
        if amount >0:
            self.__balance+=amount
        else:
            print("Invalid deposit amount")

    def withdraw(self,amount):
        if 0 < amount <=self.__balance:
            self.__balance-=amount

        else:
            print("Insufficient balance or invalid amount") 

#Usage
acc=BankAccount(1000)
print("Balance:",acc.get_balance())

acc.deposit(500)
print("accont after deposit:",acc.get_balance())

acc.withdraw(200)
print("Balance after withdrawal:",acc.get_balance())
    