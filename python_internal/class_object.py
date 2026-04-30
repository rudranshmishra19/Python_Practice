class pet:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def speak(self):
        print(f"my name is {self.name} and I am {self.age} years old ")


#Instance 
cat=pet("Meow",53)
dog=pet("brown",66)

print(isinstance(cat,pet))


# shortest way to create a class
class Empty:pass
