from abc import ABC, abstractmethod

class withdraw(ABC):
    
    @abstractmethod
    def pay(self,amount): # just define no implementation
        pass 

class cash(withdraw):
    # hide implementaion
    def pay(self, amount):
        print(f"withdrawn ₹{amount}")


w=cash()
w.pay(2000)