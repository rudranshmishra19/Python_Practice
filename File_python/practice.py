class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    
    @staticmethod
    def hello():
       print("Hii world")
    def get_avg(self):
        sum=0
        for val in self.marks:
            sum+=val
        print("hi",self.name,"Your average score is :",sum/3)    



s1=student("Rudransh",[100, 87, 59])
s1.get_avg()
s1.name="Jeet"
s1.get_avg()
s1.hello()
    