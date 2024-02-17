class Country:
    def __init__(self, name:str, gdp:int, army:int, leader:str, population:int):
        self.name = name 
        self.leader = leader
        self.army = army
        self.gdp = gdp
        self.population = population
    
    def make_war(self,name_to,text):
        print(f"{self.name} {text}{name_to}")
    
    def army_conscription(self,Count):
        self.army +=Count
        print(f"{self.name} армия {self.army}")

c1 = Country("russia", 10000000,300000,"medvediev",15)       
c2 = Country("папаская область", 500,3000000,"italy",665)      
c3 = Country("uzbek", 1,3000000000000,"uzbek",1)      

c3.make_war(c1.name,"война за кортошка!!!!")
c3.make_war(c1.name,"Mirok,")
c1.army_conscription(1000000000)