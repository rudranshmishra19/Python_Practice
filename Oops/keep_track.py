class Objectcount:
    # create a count variable as class variable
    count=0

    def __init__(self):
        Objectcount.count+=1

    @classmethod
    def get_count(cls):
        return cls.count

obj1=Objectcount()        
obj2=Objectcount()

print(Objectcount.get_count()) #works

        