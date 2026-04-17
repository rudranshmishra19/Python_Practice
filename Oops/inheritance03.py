class Human:
    def __init__(self,name):
        self.name=name
    @staticmethod
    def talk():
        print("taking")

    @staticmethod
    def walk():
        print("walking")

    @staticmethod
    def swim():
        print("Swimming")

    @staticmethod
    def sleep():
        print("Sleeping")

    @staticmethod
    def watch():
        print("Watching")
    @staticmethod    
    def eat():
        print("Eating")

    @staticmethod
    def code():
        print("Coding")    

    @staticmethod
    def learn():
        print("learning")

    @staticmethod
    def dance():
        print("Dancing")



class male(Human):
    
    def __init__(self, name,age):
        super().__init__(name) 
        self.age=age

    @staticmethod
    def sleep():
        print("He is sleeping")

    @staticmethod
    def eat():
        print("He is eating")

    @staticmethod
    def talk():
        print("He is talking to gauri")
    @staticmethod
    def code():
        print("He is currently doing projects in django")
   
            

class female(Human):
    def __init__(self, name,age):
        super().__init__(name)
        self.age=age
    @staticmethod
    def sleep():
        print("She is sleeping")

    @staticmethod
    def dance():
        print("she is dancing")     



fe=female("shiva",24)
ml=male("Kapi",23)

print(fe.name,fe.age)
print(ml.name,ml.age)


print()
print("Kapi current status ")
ml.sleep()
print("Kapi current status ")
ml.code()

print("Gauri current status")
fe.dance()




