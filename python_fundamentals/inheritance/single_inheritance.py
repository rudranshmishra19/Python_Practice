class Animal:
    def eats(self):
        print("This animal eats food ")
        
class dog(Animal):
    def speak(self):
        print("The dog barks")

class cat(Animal):
    def speak(self):
        print("The cat Meow")

#creating an object
  

Dog=dog()
Dog.speak()
Dog.eats()

Cat=cat()
Cat.speak()
Cat.eats()