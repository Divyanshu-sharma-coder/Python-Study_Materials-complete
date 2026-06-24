from abc import ABC, abstractmethod
import random
from enum import Enum, auto

class Choice(Enum):
    ROCK = auto()
    PAPER = auto()
    SCISSORS = auto()

class GameRules:
    """Encapsulates the rules and win/loss logic."""
    _WINNING_COMBINATIONS = {
        Choice.ROCK: Choice.SCISSORS,
        Choice.PAPER: Choice.ROCK,
        Choice.SCISSORS: Choice.PAPER
    }

    @classmethod
    def determine_winner(cls, choice1: Choice, choice2: Choice) -> int:
        """
        Returns:
             1 if choice1 wins
            -1 if choice2 wins
             0 for a tie
        """
        if choice1 == choice2:
            return 0
        return 1 if cls._WINNING_COMBINATIONS[choice1] == choice2 else -1

class Player(ABC):
    """Abstract Base Class representing a generic player."""
    def __init__(self, name: str):
        self.__name = name
        self.__score = 0

    @property
    def name(self) -> str:
        return self.__name

    @property
    def score(self) -> int:
        return self.__score

    def increment_score(self) -> None:
        self.__score += 1

    @abstractmethod
    def take_turn(self) -> Choice:
        """Must be implemented by subclasses to return a Choice."""
        pass

class HumanPlayer(Player):
    """Concrete implementation for a human user."""
    def take_turn(self) -> Choice:
        print("\n--- Your Turn ---")
        for choice in Choice:
            print(f"{choice.value}: {choice.name.title()}")
            
        while True:
            try:
                user_input = int(input("Enter the number of your choice: "))
                return Choice(user_input)
            except (ValueError, KeyError):
                print("Invalid input. Please enter 1, 2, or 3.")

class ComputerPlayer(Player):
    """Concrete implementation for an AI opponent."""
    def take_turn(self) -> Choice:
        return random.choice(list(Choice))

class GameEngine:
    """Controls the main state and execution loop of the game."""
    def __init__(self, player1: Player, player2: Player, target_score: int = 3):
        self.p1 = player1
        self.p2 = player2
        self.target_score = target_score
        self.current_round = 1

    def _play_round(self) -> None:
        print(f"\n=== Round {self.current_round} ===")
        c1 = self.p1.take_turn()
        c2 = self.p2.take_turn()

        print(f"{self.p1.name} chose: {c1.name}")
        print(f"{self.p2.name} chose: {c2.name}")

        result = GameRules.determine_winner(c1, c2)

        if result == 1:
            print(f"🎉 {self.p1.name} wins the round!")
            self.p1.increment_score()
        elif result == -1:
            print(f"🎉 {self.p2.name} wins the round!")
            self.p2.increment_score()
        else:
            print("🤝 It's a tie!")

        print(f"Score: {self.p1.name} [{self.p1.score}] - [{self.p2.score}] {self.p2.name}")
        self.current_round += 1

    def start_game(self) -> None:
        print(f"🚀 Starting Rock-Paper-Scissors! First to {self.target_score} wins.")
        
        while self.p1.score < self.target_score and self.p2.score < self.target_score:
            self._play_round()

        winner = self.p1 if self.p1.score == self.target_score else self.p2
        print(f"\n🏆 {winner.name} WINS THE GAME TOURNAMENT! 🏆")

if __name__ == "__main__":
    # Setup and inject dependencies
    human_name = input("Enter your name: ").strip() or "Player 1"
    user = HumanPlayer(human_name)
    ai = ComputerPlayer("CPU-9000")
    
    # Initialize the engine
    game = GameEngine(player1=user, player2=ai, target_score=3)
    game.start_game()
