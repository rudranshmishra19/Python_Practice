class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Human:
    def speak(self):
        return "Hello!"

#polymorphism with duck typing 
def make_it_speak(entity):
    print(entity.speak())

#Different objects, same method call

dog=Dog()
cat=Cat()
human=Human()
 
make_it_speak(dog)  #Woof!
make_it_speak(cat)  #Meow
make_it_speak(human) #Hello!