from random import randint
class train:
    
    # Seats=122  #defing class variable 
    # fare="$45"
    # ticket="3A UB"
    
    def __init__(self,trainNo):
                self.Train_no=trainNo
               
    
    def book(self,fro,to):
            print(f"Train No {self.Train_no} is booked form {fro} to {to}")
  
    def status (self):
            print(f"Train No {self.Train_no} is running late by 30 minutes")           
  
    def fare(self,fro,to):
            print(f"Train No {self.Train_no}  form {fro} to {to} fare is {randint(500 ,5000)}")
         
             


ticket=train(13201)
ticket.book("kalyan","Patna")
ticket.status()
ticket.fare("Kalyan","Patna")


