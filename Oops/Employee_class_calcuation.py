class Employee:
    def __init__(self,name, salary,performance_rating):
        self.name=name
        self.salary=salary
        self.performance_rating=performance_rating

    def calculate_bonus(self):
        # Default bonus =10%salarry
        if self.performance_rating=="Excellent":
           return self.salary*0.20
        elif self.performance_rating=="Good":
            return self.salary*0.15
        elif self.performance_rating=="Average":
            return self.salary*0.10
        else:
            return self.salary*0.05
          
    def __str__(self):
        return f"Employee :{self.name}, Salary:{self.salary}, Bonus: {self.calculate_bonus()}"


# Example usage
emp1=Employee("Rudransh",50000,"Good")
emp2=Employee("Meet",10000,"Average")
print(emp1)
print(emp2)