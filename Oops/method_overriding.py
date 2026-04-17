class Animal:
    def sound(self):
        print("Animal make different sounds")

#Child class
class Dog(Animal):
    #Overriding parent method
    def sound(self):
        print("Woof! Woof!")

#Child class
class Cat(Animal):
    def sound(self):
        print("Meow!")


#Objects
a=Animal()
d=Dog()
c=Cat()

a.sound()
d.sound()
c.sound()