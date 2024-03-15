class Phone:
    def __init__(self, name:str, processor:str, camera:str, memory:str):
        self.name = name 
        self.proccesor = processor
        self.camera = camera
        self.memory = memory
    
    def make_photo(self):
        print(f"{self.name} делает фото")
    
    def call(self):
        print(f"{self.name} call")
                
phone1 = Phone("Sony","Shapdragon", 50, 512)
phone2 = Phone("Iphone", " Mi", 12, 64)
print(phone1.name)
print(phone2.name)
phone2.make_photo()

class Human:
    def __init__(self, name, surnname, age, weight, growth):
        self.name = name
        self.surname = surnname
        self.weight = weight
        self.age = age
        self.growt = growth
        
    def birtsday(self):
        self.age += 1
        print(f"{self.name}, happy ef __init__(self, name, surnname, age, weight, growth):ef __init__(self, name, surnname, age, weight, growth):ef __init__(self, name, surnname, age, weight, growth):")
        
    Human = Human("gjrjgirigrgr")
    Human.birtsday()