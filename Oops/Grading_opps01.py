#Grading Scale
GRADE_SCALE={
    'A':(90,100),
    'B':(80,89),
    'C':(70,79),
    'D':(60,69),
    'F':(0,59)
}

class Student:
    def __init__(self,name):
        self.name=name
        self.marks=[]
        self._average=0 #keep track of average

    def add_marks(self,score):
        if 0<=score<=100:
            self.marks.append(score)
        else:
            print("Invalid score must be 0-100")

    def average(self):
        return sum(self.marks)/len(self.marks) if self.marks else 0


    def grade(self):
        avg=self.average()
        for grade,(low,high)in GRADE_SCALE.items():
            if low<=avg<=high:
                return grade
            else:
                return "F"

    def __str__(self):
        return f"{self.name} - Avg :{self.average():.2f} ,Grade:{self.grade()}" 


#Example usage
s1=Student("Alice")
s1.add_marks(80)
s1.add_marks(70)
s1.add_marks(60)
s1.add_marks(50)
s1.add_marks(10)

print(s1)  #Alice -Avg :83.67 ,Grade :B 


       
