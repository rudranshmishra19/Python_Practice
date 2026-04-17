class BankAccount:
    def __init__(self,account_holder,balance=0):
        self.account_holder=account_holder
        self.balance=balance

    def deposit(self,amount):
        if amount >0:
            self.balance+=amount
            print(f"Deposited:{amount}.New Balance {self.balance}") 
        else:
            print("Deposit amount must be positive ")

    def withdrawal(self,amount):
        if 0<amount<self.balance:
            self.balance -=amount
            print(f"Withdraw {amount} reamaning balance is {self.balance}")
        else:
            print("The amount you are trying to withdraw is greater than balance ")    


account=BankAccount("Ravi",2000)
account.deposit(500)
account.withdrawal(1000)
