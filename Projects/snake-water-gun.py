# Rules of the game is --
# snake beats water , water beats gun and gun beats the snake

import random

def SnakeWaterGun():
    options = ["snake", "water", "gun"]
    total = 0
    high_score = 0
    computer_score = 0
    while True:
        try:
     
         user_input = str(input("Your Turn or type quit to exit ---   "))
         user_input.strip().lower()
         u = [user_input]
         c = random.choices(options)
        except ValueError:
            print("invalid option -- ")
            
            
        if(u == ["quit"]):
          print("exiting")
          print(f"your total score is {total} and High Score is {high_score} and the computers score is {computer_score}")
          break


        if((u == ["snake"] and c == ["snake"]) or (u == ["water"] and c == ["water"]) or (u == ["gun"] and c == ["gun"])):
         print(f"Your choice {u}\n")
         print(f"Computer's choice {c}\n")
         print("--This is a Draw--")
        elif((u == ["snake"] and c == ["water"]) or (u == ["water"] and  c == ["gun"]) or (u == ["gun"] and c == ["snake"])):
         print(f"Your choice {u}\n")
         print(f"Computer's choice {c}\n")
         print("--You score 1 Point--")
         total += 1
         if(total >= high_score):
          high_score = total
    
        elif((u == ["snake"] and c == ["gun"]) or (u == ["water"] and c == ["snake"]) or (u == ["gun"] and c == ["water"])):
         print(f"Your choice {u}\n")
         print(f"Computer's choice {c}\n")
         print("--You Loose--")
         computer_score += 1
        #  print(f"your total score is {total} and High Score is {high_score}")
        # elif(u == ["quit"]):
        #   print("exiting")
        #   print(f"your total score is {total} and High Score is {high_score} and the computers score is {computer_score}")
        #   break
    
    # if(total >= high_score):
    #     high_score = total
    
    total = 0
    
SnakeWaterGun()


