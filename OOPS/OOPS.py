# # i want to create a game like GTA And i am creating NPC'S so in Procedural Programming what am i do is --

# npc1_name = "Mike"
# npc1_health = "Full"
# npc1_gun = "M416"

# npc2_name = "Lmar"
# npc2_health = "Full"
# npc2_gun = "Ak47"

# npc3_name = "Drake"
# npc3_health = "Full"
# npc3_gun = "M762"

# # and so on what if i buld 1000 npc and want to change name of 259th one complete mess thats why we use classes and objects
# # here is an example

# class ViceCity(): #This is all default values and a blueprint of a NPC 
#     name = "Swishy"
#     health = "full"
#     stamina = "full"
#     default_gun = "AK117"
#     cars = "Dacia"
#     def info(self):
#         print(f"{self.name} has {self.health} health and {self.stamina} stamina with gun {self.default_gun} and he had a car name {self.cars}")




# npc1 = ViceCity()# these are objects like a person wants a railway form with default details but in future it can change it
# npc2 = ViceCity()# these are objects like a person wants a railway form with default details but in future it can change it
# npc3 = ViceCity()# these are objects like a person wants a railway form with default details but in future it can change it

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

# npc1.info()
# npc2.info()
# npc3.info()

# # Intro to Constructor -----   so a constructor is a special type of fuction that call itself automatically withiout any explicit command
# # Making Same program using Constructor so it looks more proffessional
# print()
# print(" -----------------Constructor---------")
# print()

# class ViceCity2(): #This is all default values and a blueprint of a NPC 
#     # name = "Swishy"
#     # health = "full"
#     # stamina = "full"
#     # default_gun = "AK117"
#     # cars = "Dacia"
# # Constructor Fuction defining

#     def __init__(self, name, health, stamina, default_gun, cars):
#         self.name = name
#         self.health = health
#         self.stamina = stamina
#         self.default_gun = default_gun
#         self.cars = cars
        

#     def info(self):
#         print(f"{self.name} has {self.health} health and {self.stamina} stamina with gun {self.default_gun} and he had a car name {self.cars}")




# npc1 = ViceCity2("jake", "full", "full", "M416", "Mitsubishi")# these are objects like a person wants a railway form with default details but in future it can change it
# npc2 = ViceCity2("Drake", "full", "full", "Ak47", "suburu")# these are objects like a person wants a railway form with default details but in future it can change it
# npc3 = ViceCity2("Kendrik", "full", "full", "Aug-A3", "Alpha-Romeo")# these are objects like a person wants a railway form with default details but in future it can change it

# # npc1.info()#the values in npc1 we dont change so it prints defaultvalues


# # npc1.name = "Jake"
# # npc1.cars = "Porshe"
# # npc1.default_gun = "AWM" 

# # npc2.name = "Drake"
# # npc2.default_gun = "Vector"
# # npc2.cars = "Pagani"

# # npc3.name = "Kenya"
# # npc3.default_gun = "Mk-14"
# # npc3.cars = "Dodge-HellCat"

# npc1.info()
# npc2.info()
# npc3.info()

# print()
# print()


# print("----------------------------------------------- GETTERS & SETTERS ----------------------")
# # SO BASICALLY in our vice City class i put a new slot of currency where i stored total amount of money a user have 
# # but the issue is what if user stored -ive value like -100000 because we can modified it using npc1.currency = -10000 so we have to add a check a check that always checks first the value requirements and then modifies it and then a check that prints it
# # thats checks are called getters and setters, getters shows output wheras setter set values 
# # @property, .setter keywords we use to do this


# class ViceCity3():
#     def __init__(self, currency):
#         self._currency = currency

#     @property  #Getter
#     def currency(self):
#         return self._currency
    
#     @currency.setter #setter
#     def currency(self, value):
#         if(value < 0):
#             raise ValueError ("Currency cannot be Negative")
            
#         self._currency = value


      
# npc1 = ViceCity3(0)

# print(f"Total currency = {npc1.currency}")

# try:
#     npc1.currency = -8000
# except ValueError as e:
#     print(e)

# print(f"Total currency = {npc1.currency}")




# print()

# print("               ---------------------------------INHERITENCE-------------------------------------------               ")

# # so basically if i have a class and i want another class with same property + adding more in it then i use inheritence
# # in which we have a Parent class then its code critiria then a child class with all details of parent class + extra 


# class parent():
#     def __init__(self, name, id, age):
#         self.name = name
#         self.id = id 
#         self.age = age

#     @property 
#     def age(self):
#             return self._age
        
#     @age.setter
#     def age(self, value):
#             if(value < 0 or value > 100):
#                 raise ValueError ("Invalid age !! ")
#             self._age = value

#     @property
#     def status(self):
#          return (f"NAME : {self.name}\nid : {self.id}\n AGE : {self._age}")
 

# # try:
# #     in_name = str(input("ENTER NAME -- "))
# #     in_id = int(input("ENTER ID -- "))
# #     in_age = int(input("ENTER AGE -- "))
# #     human1 = parent(in_name, in_id, in_age)
# #     print(human1.status)
# # except ValueError as e:
# #     print(f"\nERROR {e}")


# # class child(parent):
# #     def __init__(self, name, id, age, salary):
# #         super().__init__(name, id, age)
# #         self._salary = salary

# #     @property
# #     def salary(self):
# #         return self._salary
    
# #     @salary.setter
# #     def salary(self, value):
# #         if(value < 0):
# #             raise ValueError  ("Invalid Salary !!")
# #         self._salary = value
# #     @property
# #     def show(self):
# #          return (f"\nNAME : {self.name}\nID : {self.id}\n AGE : {self._age}\n SALARY : {self._salary}")
    

# # try:
# #     in_name = str(input("ENTER NAME -- "))
# #     in_id = int(input("ENTER ID -- "))
# #     in_age = int(input("ENTER AGE -- "))
# #     in_salary = int(input("ENter Salary -- "))
# #     human2 = child(in_name, in_id, in_age, in_salary)
# #     print(human2.show)
# # except ValueError as e:
# #     print(f"\nERROR {e}")


        



# # A CATCH OF OOPS CLASSES AND OBJECTS
# # SO Basically when i make a class 
# class test():
#     pass

# a = test()
# a.age = 5
# print(a.age)
# # This will gives a ouput even i dont give attribue output so tp stop this we can just use __slot__ and fix class attributes like this

# class fix():
#     __slots__ = ("name", "age", "id")

# b= fix()
# # b.salary = 50000
# # Now this will throws and error.................
 


# print()
# print("---------------------------------- STATIC METHODS -----------------------------------------")
# # In class when we create any function even a constructor so we use a self keyword that pass the instance of that class as an argument in that function --
# # but what if i want to use just a fuction like add return(a+b) and i need to pass self in it also so when i call that fuction instance will also pass and interpreter got confused coz first it got 3 args and second like in instance we have a name variable then the inter preter confused how to add "miks" + 20+20 and got error
# # so thats why we use STATIC METHODS it gave us a self keyword less function 




# class childViceCity3(ViceCity3):
#     def __init__(self, currency, age):
#         super().__init__(currency)
#         self._age = age

#     @property
#     def age(self):
#         return self._age
    
#     @age.setter
#     def name(self, value):
#         if(value < 0 or value > 100):
#             raise ValueError ("Please Enter Valid Age :- ")
#         self._age = value

#     @staticmethod
#     def square(a):
#         return a*a
    
#     @property
#     def show(self):
#          return (f"AGE : {self._age}\n SALARY : {self._currency}\n")
    
# try:
#   in_age = int(input("ENter Age :- "))
#   in_currency = int(input("Enter Currency :- "))
#   in_a = int(input("Enter a Number to square :- "))
#   one  = childViceCity3(in_age, in_currency)

#   print(one.show)
#   print(one.square(in_a))

# except ValueError as e:
#     print(f"\nERROR : {e}")




# # Class Variable vs Instance Variabele
# print("----------------------------------Class Variable V/S Instance Variable------------------------------------")
# class company():
#     companyName = "Nvidia" # Class Variables
#     def __init__(self):
#         self.name = "Mike"
#         self.id = 1

#     @property
#     def showinfo(self):
#         print(f"Employee name {self.name} with id {self.id} is working on {self.companyName}")
    
# try:
#     emp1 = company()
#     emp1.name = "Divyanshu"#Instance Variable
#     emp1.id = 2006#Instance Variable
#     emp1.showinfo


#     emp2 = company()
#     emp2.name = "Honey"
#     emp2.id = 2008
#     emp2.showinfo

# # Above code give same company name but what if i do this --
#     emp2.companyName = "Google DeepMind"
#     emp2.showinfo
# # Now you see Honey is now works on Google Deepmind and Divyanshu is still in Nvidia so its like class Variable is a Default value that you can change at Instance but if you don't this value stays default we use this in our above ViceCity class

# except ValueError as e:
#     print(f"\nERROR - {e}")

print("--------------------------------------Class Methods---------------------------------------------")
# Understand this with an example

class game():
    FavouriteGame = "God of War : Record of Ragnarok" #class Variable
    
    def showinfo(self):
        print(f"The favourite game name is {self.FavouriteGame}") # function for showing the info.

    # def changeGame(cls, Favourite):
    #     cls.FavouriteGame = Favourite # Normal Funtion to change the game preference from god of war to another one

    @classmethod
    def changeGame(cls, Favourite):
        cls.FavouriteGame = Favourite #class method to change the Game preference from god wo war to another one

game1 = game() #object for class game 

game1.showinfo() # output :- The favourite game name is God of War : Record of Ragnarok
game1.changeGame("Call of Duty - ModernWarfare 4") #Instance variable that change instance
game1.showinfo() # output :- The favourite game name is Call of Duty - ModernWarfare 4
print(game.FavouriteGame) # COD MW 4

# Now the real answer why we use Clss method is that when i am just using an ordinary function and then change the FavouriteGame using instance variable and then print(game.FavouriteGame) the output is God of war even after changing it why because the favouriteGame stored in a class Variable and if we need to change that we have to use classmethod-- so that's what i do above


print()
print("----------------------Class Methods as Alternative Constructors----------------------------------")
# Also called additional Constructors 
# so basically in our previous class i have a new variable currentlyPlayedGame and hours he play but all that data comes in this form like this ("red dead redemption-2-GTA V-4")
# So i need to do this

class Game():
    def __init__(self, currentlyPlayedGame, hours):
        self._currentlyPlayedGame = currentlyPlayedGame 
        self._hours = hours

    @property   
    def showInfo(self):
        print(f"Currently he is playing {self._currentlyPlayedGame} for {self._hours} hours")

    @classmethod
    def change(cls, string):
        return cls((string.split("-")[0]), int(string.split("-")[1]))

string = "RedDeadRedemption-2-GTAV-4"  
game1 = Game.change(string)
game1.showInfo









































