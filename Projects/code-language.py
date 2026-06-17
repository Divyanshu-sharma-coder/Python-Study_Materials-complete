import random
import string

# Rule 1: Move functions outside of the main loop
def code_language():
    """
    This Function is used to convert normal language into a Code Language using a set of rules:
    1. Remove the first letter of the word and append it to the end of the word.
    2. Then add 3 random characters at the starting and the ending of the word.
    """
    all_letters = string.ascii_letters

    a = str(input("Enter a word to code it into our code Language: "))
    b = a.strip().lower()

    if not b:
        print("Please enter a valid input")
        return # Use return to exit this specific run back to the main menu

    if b == "quit":
        print("Returning to main menu...")
        return

    if len(b) >= 3:
        c = b[0]
        result = b[1:]
        output = result + c
        random_characters = "".join(random.choices(all_letters, k=3))
        random_character2 = "".join(random.choices(all_letters, k=3))

        right_side = random_characters + output
        left_side = right_side + random_character2
        coded_word = left_side.lower()
        
        print("Coded word:", coded_word)
    else:
        print("Coded word:", b[::-1])


def decode_language():
    a = str(input("Enter a word to decode: "))
    b = a.strip().lower()

    if not b:
        print("Please enter a valid word.")
        return

    if b == "quit":
        print("Returning to main menu...")
        return

    # Words less than 3 characters were just reversed
    if len(b) < 3:
        decoded_word = b[::-1]
        print("Decoded word:", decoded_word)
    
    # Words with 3 or more characters have random padding and a shifted letter
    else:
        stripped = b[3:-3]
        
        if len(stripped) > 0:
            original_first_letter = stripped[-1]
            rest_of_word = stripped[:-1]
            decoded_word = original_first_letter + rest_of_word
            print("Decoded word:", decoded_word)
        else:
            print("Error: The message is too short or invalid to decode.")


# --- MAIN MENU LOOP ---
while True:
    try:
        user_choice = str(input("\nWhat do you want to do? (Encode / Decode / Quit) ===> "))
        # Rule 2: You must re-assign the modified string back to the variable
        user_choice = user_choice.strip().lower() 
    except ValueError:
        print("Invalid option please select between Encode, Decode, or Quit!")
        continue

    if user_choice == "encode":
        code_language() # Rule 4: Called normally without printing a blank return
    elif user_choice == "decode":
        decode_language() # Rule 4: Added missing parentheses ()
    elif user_choice == "quit":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid option! Please try again.")
