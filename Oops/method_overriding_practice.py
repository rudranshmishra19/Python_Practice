class Bird:
    def sound(self):
        print("Birds chirp ")

class Sparrow(Bird):
    def sound(self):
        super().sound()  #calls parent method
        print("Sparrow chirps sweetly")

sparrow=Sparrow()
sparrow.sound()
