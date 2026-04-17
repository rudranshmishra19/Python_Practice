class BankAccount:
    def __init__(self,owner,balance):
        self.owner=owner
        self._balance=balance
    
    def deposit(self,amount):
        if amount >0:
            self._balance+=amount
            print(f"Deposited {amount} updated balance is {self._balance}")

    def withdraw(self,amount):
        if amount<=self._balance:
            self._balance-=amount
            print(f"sucessfully withdrawn {amount} avaliable balance {self._balance}")
        else:
            print("insufficient balance")

    def show_balance(self):
        print(f"Owner:{self.owner} | Balance :{self._balance}")

    def add_interest(self,interest,period):
        si= (period*self._balance*interest)/100
        print(f"Interest added:{si} | New balance: {self._balance}")
        self._balance+=si
        return si
            
class SavingsAccount(BankAccount):
    def __init__(self, owner, balance,interest_rate):
        super().__init__(owner, balance)
        self.interest_rate=interest_rate  #sirf store 

    def apply_interest(self):
        self.add_interest(self.interest_rate,1)  #parent ka method



class CurrentAccount(BankAccount):
    def __init__(self, owner, balance,overdraft_limit):
        super().__init__(owner, balance)
        self.overdraft_limit=overdraft_limit
    
    def withdraw(self, amount):
        if amount <= self._balance + self.overdraft_limit:
            self._balance -= amount
            print(f"Withdrawn {amount} | Balance: {self._balance}")
        else:
             print("Exceeds overdraft limit!")

HDFC=BankAccount("Rudransh",200000)
HDFC.show_balance()
HDFC.deposit(30000)
HDFC.withdraw(4000)
HDFC.add_interest(interest=2,period=2)

#saving account tesst
HDFC=SavingsAccount("Rudransh",10000,5)
HDFC.show_balance()
HDFC.apply_interest()
HDFC.show_balance()

#CurrentAccount Test
HDFC=CurrentAccount("Rudransh",5000,1000)
HDFC.show_balance()
HDFC.withdraw(4000)
HDFC.withdraw(20000)
