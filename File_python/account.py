class Account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account_no=acc
    def debit(self,amount):
        if 0<amount<self.balance:
            self.balance-=amount
            return f"Debited {amount}.New Balance:{self.balance}"
        else:
            return f"insuffic balance"

    def credit(self,amount):
        if amount>0 :
            self.balance+=amount
            return f"Credited {amount}.New Balance:{self.balance}"
        else:
            return "Invalid credit amount " 

    def check_balance(self):
        return f"Current balance:{self.balance} "

acc1=Account(10000,12345)
print(acc1.check_balance())
print(acc1.debit(400))
print(acc1.credit(1000))
print(acc1.check_balance())



