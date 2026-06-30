from abc import ABC, abstractmethod
import random
import time

class Ability:
    """Class representing a special combat action (Composition)."""
    def __init__(self, name: str, damage_multiplier: float, energy_cost: int):
        self.name = name
        self.damage_multiplier = damage_multiplier
        self.energy_cost = energy_cost

    def execute(self, base_damage: int) -> int:
        return int(base_damage * self.damage_multiplier)


class Entity(ABC):
    """Abstract Base Class enforcing the blueprint for all game characters."""
    def __init__(self, name: str, health: int, energy: int, base_damage: int):
        self.name = name
        self._health = health          # Protected attribute (Encapsulation)
        self._max_health = health
        self.energy = energy
        self.base_damage = base_damage
        self.abilities = []

    @property
    def is_alive(self) -> bool:
        """Getter to check entity status."""
        return self._health > 0

    @property
    def health_status(self) -> str:
        """Returns a scannable health bar string."""
        return f"{self.name}: {self._health}/{self._max_health} HP"

    def take_damage(self, amount: int):
        """Standardized damage intake system."""
        self._health = max(0, self._health - amount)
        print(f"💥 {self.name} takes {amount} damage!")

    @abstractmethod
    def take_turn(self, opponent: 'Entity'):
        """Polymorphic method; behavior depends entirely on the subclass."""
        pass


class Player(Entity):
    """The Hero subclass representing the user's starship."""
    def __init__(self, name: str):
        super().__init__(name=name, health=120, energy=50, base_damage=15)
        # Equip unique tactical abilities
        self.abilities = [
            Ability("Plasma Cannon", damage_multiplier=1.8, energy_cost=20),
            Ability("Nano-Swarm Repair", damage_multiplier=-1.2, energy_cost=15) # Negative damage = heal
        ]

    def take_turn(self, opponent: Entity):
        print(f"\n--- {self.name}'s TURN ---")
        print(f"HP: {self._health}/{self._max_health} | Energy: {self.energy} EN")
        print("1. Standard Laser Attack\n2. Use Ability\n3. Recharge Energy")
        
        choice = input("Select your action (1-3): ").strip()

        if choice == "1":
            print(f"🛰️ {self.name} fires standard lasers!")
            opponent.take_damage(self.base_damage)
        
        elif choice == "2":
            print("\nAvailable Abilities:")
            for i, ab in enumerate(self.abilities, 1):
                print(f"  {i}. {ab.name} [Cost: {ab.energy_cost} EN]")
            
            try:
                ab_choice = int(input("Select Ability: ")) - 1
                selected_ability = self.abilities[ab_choice]
                
                if self.energy >= selected_ability.energy_cost:
                    self.energy -= selected_ability.energy_cost
                    power = selected_ability.execute(self.base_damage)
                    
                    if power < 0: # Healing action
                        self._health = min(self._max_health, self._health - power)
                        print(f"🔧 {self.name} activates {selected_ability.name} and repairs for {-power} HP!")
                    else:
                        print(f"⚡ {self.name} unleashes {selected_ability.name}!")
                        opponent.take_damage(power)
                else:
                    print("❌ Not enough energy! Standard lasers fired instead.")
                    opponent.take_damage(self.base_damage)
            except (ValueError, IndexError):
                print("❌ Invalid input! Action missed due to system error.")
        
        else:
            self.energy += 25
            print(f"🔋 {self.name} shields up and recharges +25 Energy!")


class Enemy(Entity):
    """The automated Adversary subclass."""
    def __init__(self, name: str, health: int, base_damage: int):
        super().__init__(name=name, health=health, energy=30, base_damage=base_damage)
        self.abilities = [Ability("Overcharge Beam", damage_multiplier=2.0, energy_cost=15)]

    def take_turn(self, opponent: Entity):
        print(f"\n--- {self.name}'s TURN ---")
        time.sleep(1) # Dramatic pacing
        
        # Simple AI decision-making matrix
        if self.energy >= 15 and random.random() > 0.4:
            self.energy -= 15
            power = self.abilities[0].execute(self.base_damage)
            print(f"🛑 {self.name} fires a devastating {self.abilities[0].name}!")
            opponent.take_damage(power)
        else:
            print(f"👾 {self.name} lunges forward with a basic strike!")
            opponent.take_damage(self.base_damage)


class GameEngine:
    """Manager class that handles the core loop, instantiation, and state orchestration."""
    def __init__(self):
        print("🌌 WELCOME TO OOP CYBERPUNK SPACE ARENA 🌌")
        player_name = input("Enter your Pilot Name: ").strip() or "Ace"
        self.player = Player(player_name)
        
        # Generating a list of enemies for a ladder-based challenge loop
        self.enemy_pool = [
            Enemy("Scrap Drone", health=50, base_damage=8),
            Enemy("Void Reaver", health=80, base_damage=12),
            Enemy("Dreadnought Core", health=150, base_damage=18)
        ]

    def start(self):
        """Launches the primary gameplay iteration loop."""
        for round_num, enemy in enumerate(self.enemy_pool, 1):
            print(f"\n=================================")
            print(f"🚀 ROUND {round_num}: Encountering {enemy.name}!")
            print(f"=================================")
            
            while self.player.is_alive and enemy.is_alive:
                print(f"\n📊 Status -> {self.player.health_status} | {enemy.health_status}")
                
                # Player moves
                self.player.take_turn(enemy)
                if not enemy.is_alive:
                    print(f"\n🏆 You destroyed {enemy.name}!")
                    self.player.energy += 15 # Reward energy
                    break
                
                # Enemy moves
                enemy.take_turn(self.player)
                if not self.player.is_alive:
                    print(f"\n💀 Your ship exploded. Game Over.")
                    return
                
        print("\n🎉 CONGRATULATIONS! You cleared the arena and saved the sector!")


# Global entry point executing the game system
if __name__ == "__main__":
    game = GameEngine()
    game.start()
