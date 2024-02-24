import random

class Fither:
    def __init__(self, name:str, name_fatality:str):
        self.name = name
        self.power = random.radiant(1,5)
        self.hp = 100
        self.name_fat = name_fatality
    
Fither1 = Fither("skorp","syper makak")
Fither2 = Fither("oladyshki","cok")
Fither3 = Fither("kyng fy panada","skill")

Fithers =[Fither1,Fither2,Fither3]
    