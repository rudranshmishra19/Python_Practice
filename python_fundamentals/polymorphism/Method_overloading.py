class claculator:
    def add(self,a,b=0,c=0):
        return a+b+c
    
calc=claculator()
print(calc.add(5))
print(calc.add(5,10))
print(calc.add(5,10,13))
