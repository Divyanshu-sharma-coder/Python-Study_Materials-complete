# i want to create a game like GTA And i am creating NPC'S so in Procedural Programming what am i do is --

npc1_name = "Mike"
npc1_health = "Full"
npc1_gun = "M416"

npc2_name = "Lmar"
npc2_health = "Full"
npc2_gun = "Ak47"

npc3_name = "Drake"
npc3_health = "Full"
npc3_gun = "M762"

# and so on what if i buld 1000 npc and want to change name of 259th one complete mess thats why we use classes and objects
# here is an example

class ViceCity(): #This is all default values and a blueprint of a NPC 
    name = "Swishy"
    health = "full"
    stamina = "full"
    default_gun = "AK117"
    cars = "Dacia"
    def info(self):
        print(f"{self.name} has {self.health} health and {self.stamina} stamina with gun {self.default_gun} and he had a car name {self.cars}")




npc1 = ViceCity()# these are objects like a person wants a railway form with default details but in future it can change it
npc2 = ViceCity()# these are objects like a person wants a railway form with default details but in future it can change it
npc3 = ViceCity()# these are objects like a person wants a railway form with default details but in future it can change it

npc1.info()#the values in npc1 we dont change so it prints defaultvalues


npc1.name = "Jake"
npc1.cars = "Porshe"
npc1.default_gun = "AWM" 

npc2.name = "Drake"
npc2.default_gun = "Vector"
npc2.cars = "Pagani"

npc3.name = "Kenya"
npc3.default_gun = "Mk-14"
npc3.cars = "Dodge-HellCat"

npc1.info()
npc2.info()
npc3.info()

# Intro to Constructor -----   so a constructor is a special type of fuction that call itself automatically withiout any explicit command
# Making Same program using Constructor so it looks more proffessional
print()
print(" -----------------Constructor---------")
print()

class ViceCity2(): #This is all default values and a blueprint of a NPC 
    # name = "Swishy"
    # health = "full"
    # stamina = "full"
    # default_gun = "AK117"
    # cars = "Dacia"
# Constructor Fuction defining

    def __init__(self, name, health, stamina, default_gun, cars):
        self.name = name
        self.health = health
        self.stamina = stamina
        self.default_gun = default_gun
        self.cars = cars
        

    def info(self):
        print(f"{self.name} has {self.health} health and {self.stamina} stamina with gun {self.default_gun} and he had a car name {self.cars}")




npc1 = ViceCity2("jake", "full", "full", "M416", "Mitsubishi")# these are objects like a person wants a railway form with default details but in future it can change it
npc2 = ViceCity2("Drake", "full", "full", "Ak47", "suburu")# these are objects like a person wants a railway form with default details but in future it can change it
npc3 = ViceCity2("Kendrik", "full", "full", "Aug-A3", "Alpha-Romeo")# these are objects like a person wants a railway form with default details but in future it can change it

# npc1.info()#the values in npc1 we dont change so it prints defaultvalues


# npc1.name = "Jake"
# npc1.cars = "Porshe"
# npc1.default_gun = "AWM" 

# npc2.name = "Drake"
# npc2.default_gun = "Vector"
# npc2.cars = "Pagani"

# npc3.name = "Kenya"
# npc3.default_gun = "Mk-14"
# npc3.cars = "Dodge-HellCat"

npc1.info()
npc2.info()
npc3.info()

































