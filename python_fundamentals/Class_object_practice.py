#defining a class 
class sutherland:
        def __init__(self,name,company,emp_id):   #construct name ,company, emp i 
                self.name=name
                self.company=company 
                self.emp_id=emp_id

        def greet(self):  # define method
             print(f"Hello! {self.name},Your id is {self.emp_id}")        
             print(f"You work at {self.company}")        
#Creating an object
my_company=sutherland("Rudransh","AT&T","620710")
omkar_company=sutherland("Omkar","Netflix","53553")

print(f"I work in {my_company.company} Company") #access the 'Company ' Attribute 
print(f"Omkar works  in {omkar_company.company} Company") #access the 'Company ' Attribute 
print(" ")
my_company.greet()   #call the function in class
omkar_company.greet()  

