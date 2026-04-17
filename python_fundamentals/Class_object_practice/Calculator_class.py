#defining a calculator class
class calculator:
      #defining for constructor
      def __init__(self,n):
             self.n=n
       #defining method for instance
      def square(self):
        print(f"The square is {self.n * self.n}")
      def cube(self):
        print(f"The cube is {self.n * self.n*self.n}")
      def square_root(self):
        print(f"The square root is {self.n**0.5}")
        
      @staticmethod
      def greet():
        return "hello! there"  #get staticmethod
#calling staticmethod      
print(calculator.greet())
#calling instance method
a=calculator(64)
a.square()
a.cube()
a.square_root()