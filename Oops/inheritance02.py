class Moblie:
    @staticmethod
    def charge():
        print("Charged....")
    @staticmethod
    def discharge():
        print("Discharged....")
    @staticmethod
    def wake_screen():
        print("Screen_waked")
    @staticmethod
    def sleep_screen():
        print("Screen_slept")

class Samsung_phone(Moblie):
    def __init__(self,name):
        self.name=name


sam=Samsung_phone("Samsung_galaxys23Ultra")
print(sam.name)
sam.sleep_screen(),sam.wake_screen(),sam.discharge()




        
