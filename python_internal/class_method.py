class Human:
     total_population=0 #class variable

     def __init__(self,name):
          self.name=name
          Human.total_population+=1

     @classmethod
     def get_total(cls):
               return f"Total Population: {cls.total_population}"
     
Human.get_total()
print(Human.get_total())

human=Human("Rudransh")
human2=Human("Shreya")
print(human.get_total())
