class Sharingan:
    def __init__(self,copy,predictive):
        self.eye=copy,predictive
       

class Mangekyou_Sharingan(Sharingan):
    def __init__(self, copy, predictive,Tsukuymoi,Amaterasu,Susanoo):
        super().__init__(copy, predictive)
        self.tsukuyomi=Tsukuymoi
        self.Amaterasu=Amaterasu
        self.Susanoo=Susanoo

# Base Sharingan
itachi=Sharingan(copy="can copy any jutus",predictive="can predict opponent's moves")
# Advanced sharingan
itachi=Mangekyou_Sharingan(
    copy="can copy any jutus",
    predictive="can predict opponent's move",
    Tsukuymoi="Can trap anyone in illusion",
    Amaterasu="Can release black flames",
    Susanoo="Build massive monster sheild to protect and attack"
)

print(itachi.eye)
print(itachi.tsukuyomi)
print(itachi.Amaterasu)
print(itachi.Susanoo)