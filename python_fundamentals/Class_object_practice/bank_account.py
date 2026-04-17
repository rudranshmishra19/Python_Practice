class bank_account:
    def __init__(self,account_number,balance):
          self.account_number=account_number  #public
          self._bank_name="HDFC BANK"   #protected
          self.__balance=balance     #private


    #  public method to get access to balance
    @property
    def get_balance(self):  #getter
        return self.__balance
    
    @get_balance.setter
    def get_balance(self,amount):
         if amount>=0:
              self.__balance=amount
         else:
              print("Invalid balance!")       

    # public method to get access to bank name
    @property
    def get_name(self): #geter
         return self._bank_name    
    
      
#creating an instance  
Bank=bank_account(100140310310,50000)
print(Bank.get_balance)
Bank.get_balance=90000   
print(Bank.get_balance)
print(Bank.get_name)
print(f"Account {Bank.account_number}")
#print(f"The account number is {bank_account.get_account_Num()}")
