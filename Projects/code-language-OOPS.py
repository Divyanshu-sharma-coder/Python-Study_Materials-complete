import abc
import random
import string
from typing import Final, Protocol



class CipherStrategy(abc.ABC):
    """Abstract Base Class defining the interface for text transformation."""
    
    @abc.abstractmethod
    def transform(self, text: str) -> str:
        """Apply transformation algorithm to the given text."""
        pass


class UserInterface(Protocol):
    """Structural protocol defining required capabilities for the application UI."""
    
    def get_input(self, prompt: str) -> str: ...
    def display_message(self, message: str) -> None: ...
    def display_error(self, error: str) -> None: ...



class SecretLanguageCipher(CipherStrategy):
    """Handles logic for encoding and decoding based on custom language rules."""
    
    MIN_COMPLEX_LENGTH: Final[int] = 3
    PADDING_LENGTH: Final[int] = 3

    def __init__(self) -> None:
        self._alphabet: str = string.ascii_letters

    def _generate_padding(self) -> str:
        """Helper to generate random cryptographic character padding."""
        return "".join(random.choices(self._alphabet, k=self.PADDING_LENGTH))

    def transform(self, text: str) -> str:
        """Polymorphic entry point; defaults to encoding logic."""
        return self.encode(text)

    def encode(self, text: str) -> str:
        """Encodes a word using shifting and random letter padding rules."""
        clean_text = text.strip().lower()
        if not clean_text:
            return ""
            
        if len(clean_text) < self.MIN_COMPLEX_LENGTH:
            return clean_text[::-1]

        # Shift first character to the end
        shifted = clean_text[1:] + clean_text[0]
        # Pad both sides
        prefix = self._generate_padding()
        suffix = self._generate_padding()
        
        return f"{prefix}{shifted}{suffix}".lower()

    def decode(self, text: str) -> str:
        """Decodes a word by stripping padding and reversing the character shift."""
        clean_text = text.strip().lower()
        if not clean_text:
            return ""

        if len(clean_text) < self.MIN_COMPLEX_LENGTH:
            return clean_text[::-1]

        # Strip 3 characters from start and 3 from end
        stripped = clean_text[self.PADDING_LENGTH : -self.PADDING_LENGTH]
        if not stripped:
            raise ValueError("Message payload is missing or structurally corrupted.")

        # Reconstruct by moving the last letter back to the front
        original_first_letter = stripped[-1]
        rest_of_word = stripped[:-1]
        
        return f"{original_first_letter}{rest_of_word}"




class ConsoleInterface:
    """Handles standard I/O communication operations with the end-user."""
    
    def get_input(self, prompt: str) -> str:
        return input(prompt).strip().lower()

    def display_message(self, message: str) -> None:
        print(f"\n[INFO] {message}")

    def display_error(self, error: str) -> None:
        print(f"\n[ERROR] {error}")




class CipherApplication:
    """Main Orchestrator using Dependency Injection to tie UI and Logic together."""
    
    def __init__(self, cipher: SecretLanguageCipher, ui: UserInterface) -> None:
        self._cipher = cipher
        self._ui = ui
        self._is_running = False

    def run(self) -> None:
        """Starts the main execution engine loop."""
        self._is_running = True
        self._ui.display_message("Secret Language Engine Initialised.")
        
        while self._is_running:
            try:
                choice = self._ui.get_input(
                    "\nWhat do you want to do? (Encode / Decode / Quit) ===> "
                )
                self._process_command(choice)
            except Exception as e:
                self._ui.display_error(f"An unexpected system exception occurred: {e}")

    def _process_command(self, command: str) -> None:
        """Route user choice inputs to respective specialized engine methods."""
        if command == "encode":
            self._handle_encode_flow()
        elif command == "decode":
            self._handle_decode_flow()
        elif command == "quit":
            self._ui.display_message("Exiting program. Goodbye!")
            self._is_running = False
        else:
            self._ui.display_error("Invalid option! Please select Encode, Decode, or Quit.")

    def _handle_encode_flow(self) -> None:
        user_input = input("Enter a word to code it into our code Language: ")
        if not user_input.strip():
            self._ui.display_error("Please enter a valid input.")
            return
        if user_input.strip().lower() == "quit":
            self._ui.display_message("Returning to main menu...")
            return

        result = self._cipher.encode(user_input)
        print(f"Coded word: {result}")

    def _handle_decode_flow(self) -> None:
        user_input = input("Enter a word to decode: ")
        if not user_input.strip():
            self._ui.display_error("Please enter a valid word.")
            return
        if user_input.strip().lower() == "quit":
            self._ui.display_message("Returning to main menu...")
            return

        try:
            result = self._cipher.decode(user_input)
            print(f"Decoded word: {result}")
        except ValueError as err:
            self._ui.display_error(str(err))




if __name__ == "__main__":
    # Dependency Injection pattern setup
    cipher_engine = SecretLanguageCipher()
    user_ui = ConsoleInterface()
    
    # Initialize and execute system application
    app = CipherApplication(cipher=cipher_engine, ui=user_ui)
    app.run()
