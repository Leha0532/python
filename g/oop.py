class C1:
    def __init__(self):
        pass

    def decorate(self,phrase):
        print("------------")
        print(f"|{phrase}|")
        print("------------")
c1 = C1()
c1.decorate("i love oop")
    
class Father:
    def __init__(self,name:str,age:int):
        self.name = name.capitalize()
        self.age = age
        self.gender = "Мужчина"
        self.power = 0
    def swim(Self):
        print (f"{name} plavat")
    def dispute(self):
        print(f"{name} spor")
    def shoping(self):
        self.power =+ 1
        print (f"{name} rybit drov power papa = {self.power}")
        
father = Father(name="oleg", age=55)
father.swim()
father.dispute()
father.shoping()

class Son("roman",5)
Son.swim
Son.dispute
Son.choping

class Son(Father):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)

    def dispute(self):
        super().dispute()
        print(f"{self.name} sporit")
