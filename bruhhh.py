import random

class Fither:
    def __init__(self, name:str, name_fatality:str):
        self.name = name
        self.power = random.radiant(1,5)
        self.hp = 100
        self.name_fat = name_fatality
    
    def attack(self, attaked_fihter):
        attaked_fihter.hp -= self.power
        print("{self.name}наносит {self.power}ed yrona pesonazy {attaked_fighter.name}")
        
    def say_info(self):
        print(f"y person {self.name} {self.hp} ed zd {self.power}ed power")
    
    def fatal(self,attaked_fighter):
        if self.hp < 15:
            damage = random.renint(0,)
            attaked_fighter.hp -= damage
            print(f"(self.name) prim cyp {self.name_fot} nanosit (damage)ed erona pers{attaked_fighter.name}")

Fither1 = Fither("skorp","syper makak")
Fither2 = Fither("oladyshki","cok")
Fither3 = Fither("kyng fy panada","skill")

Fithers =[Fither1,Fither2,Fither3]
enemy1 =random.choice(Fithers)
Fithers.remove(enemy1)
enemy2 =random.choice(Fithers)

Fithers.append(enemy1)

print("{enemy.name} vs {enemy2.name}")

while True:
    enemy1.attack(enemy2)
    enemy2.attack(enemy1)
    enemy1.say_info()
    enemy2.say_info()
    if enemy1.hp <= 0 and enemy2.hp <= 0:
        print("draw")
        break
    elif enemy2.hp <= 0:
        print(f"{enemy1.name} win")
        break