#Defining a mutilevel class
class shape:
    def calculate_area(self):
        pass
#inherits method from class shape
class circle(shape):
    def __init__(self,radius):
        self.radius=radius

    def calculate_area(self):
        return 3.14*self.radius*self.radius

class square(shape):
    def __init__(self,side):
        self.side=side

    def calculate_area(self):
        return  self.side*self.side

class rectange(shape):
    def __init__(self,length,breadth):
         self.length=length
         self.breadth=breadth

    def calculate_area(self):
        return  self.length*self.breadth


#Creating a print_area class
class Print_area:
      @staticmethod
      def print_area(shape):
        print(f"The area of {shape.__class__.__name__} is {shape.calculate_area()}")


Cricle=circle(4)
Square=square(6)
Rectangle=rectange(10,4)


Print_area.print_area(Cricle)
Print_area.print_area(Square)
Print_area.print_area(Rectangle)