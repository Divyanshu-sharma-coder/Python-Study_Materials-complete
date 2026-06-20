# ----------------------creating a NPC using classes object and getters and setters , constructors

# Rules:

# Health cannot be less than 0
# Health cannot be greater than 100
# Level cannot be less than 1



# class ViceCity():
#     def __init__(self, health, Level):
#         self.health = health
#         self.level = Level

#     @property
#     def health(self):
#         return self._health
    
#     @property
#     def level(self):
#         return self._level



#     @health.setter
#     def health(self, value):
#         if(value < 0 or value > 100):
#             raise ValueError("The health is creating issue -- check it !!")
#         self._health = value

#     @level.setter
#     def level(self, value):
#         if(value < 1):
#             raise ValueError ("The Level is less then 1 !! Danger")
#         self._level = value

    


# npc1 = ViceCity(45, 65)
# try: 
#     print(npc1.health)
#     print(npc1.level)
#     npc1.health = int(input("Enter health : "))
#     npc1.level = int(input("Enter level : "))


# except ValueError as e:
#     print(e)


# print(npc1.health)
# print(npc1.level)



print("---------------------------------RPG WARRIOR------------")



# A more powerful Project -- RPG warrior
class Warrior():
    def __init__(self, name, health, mana, level):
        self.name = name
        self.health = health
        self.mana = mana
        self.level = level

    @property 
    def health(self):
        return self._health

    @health.setter
    def health (self, value):
        if(value < 0 or value > 100):
            raise ValueError ("Critical issue in Health--")
        self._health = value

    @property
    def mana(self):
        return self._mana
    
    @mana.setter
    def mana(self, value):
        if(value < 0 or value >= 100):
            raise ValueError ("Critical issue in mana--")
        self._mana = value

    @property
    def level(self):
        return self._level
    
    @level.setter
    def level(self, value):
        if(value < 1):
            raise ValueError ("Critical issue in level--")
        self._level = value
        
    @property
    def status(self):
        return (f"name : {self.name}\nhealth : {self._health}\nmana : {self._mana}\nlevel : {self._level}")
    

    # Total damage 
    def total_damage(self, damage):
        print()
        print(f"your player name {self.name} is taken {damage} damage")
        new_health = self.health - damage


        if(new_health < 0):
            self.health = 0
          
        else:
            self.health = new_health


        if(self.health == 0):
            print(f"{self.name} is defeated") 

    
    # Healing codes
    def Heal(self, heal_amount):
        print()
        print(f"You got medicines and you health increased about {heal_amount} points --")
        healing = self.health + heal_amount

        if(healing < 0):
            self.health = self.health
        elif(healing > 100):
            self.health = 100
        else:
            self.health = healing
        
        if(self.health == 100):
            print("Player have full health")

    # Leveling up
    def levelup(self):
        if self.mana > 90:
        # Add 1 to the current level using +=
         self.level += 1
         print(f"🎉 Level Up! {self.name} is now level {self.level}!")
         
        # Optional: Reset mana back to 0 or reduce it after leveling up
         self.mana -= 90
        else:
         print(f"⚡ Not enough mana to level up. Current mana: {self.mana}")



    # is_alive Getter 
    @property
    def is_alive(self):
        if(self.health > 0):
            return "Alive"
        else:
            return "Dead"




    
try:
    # 1. Collect inputs first
    in_name = str(input("Enter name -- "))
    in_health = int(input("Enter Health -- "))
    in_mana = int(input("Enter MANA -- "))
    in_level = int(input("Enter Level -- "))
    in_total_damage = int(input("Enter Total Damage -- "))
    in_total_heal = int(input("Enter healing amount -- "))
    # 2. Try to create the player (this triggers the setters)
    player1 = Warrior(in_name, in_health, in_mana, in_level)
    
    # 3. If creation succeeds, print the status
    print("\n--- Warrior Created Successfully ---")
    player1.total_damage(in_total_damage)
    player1.Heal(in_total_heal)
    player1.levelup()
    print(player1.status)
    print(f"The player is {player1.is_alive}")

except ValueError as e:
    # Captures invalid inputs (like typing 'abc' for health) OR setter validation failures
    print(f"\n[ERROR] {e}")




        
    
















































    














    