# We create the blueprint(class)
class Car:
    def __init__(self):
        self.color="Red"
        self.speed="60"

# 2 we build a real car from the blueprint(objects)
my_car=Car()
print(my_car.color)
