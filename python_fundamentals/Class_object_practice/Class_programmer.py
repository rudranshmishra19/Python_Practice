class programmer:
    company="Microsoft"  #defing class variable 
    @classmethod
    def get_company (cls):
         return cls.company  # Access class variable 
       
       
     #defining the constructor for instance
    def __init__(self,name,empid,level):
          self.name=name
          self.empid=empid
          self.level=level
Rudransh=programmer("Rudransh","620710",2)          
Jeet=programmer("jeet","660190",3)
Omkar=programmer("Omkar","44534",3)      
print()
print(f"Name:{Rudransh.name} Empid:{Rudransh.empid} Level:{Rudransh.level} Company:{programmer.get_company()}")    
print(f"Name:{Jeet.name} Empid:{Jeet.empid} Level: {Jeet.level} Company:{programmer.get_company()}")    
print(f"Name:{Omkar.name} Empid:{Omkar.empid} Level: {Omkar.level} Company:{programmer.get_company()}")    