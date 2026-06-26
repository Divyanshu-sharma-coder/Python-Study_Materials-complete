#  Wa;rus Operator 

# so why we need it because -----
# if i want to erite this expression

name = input('Enter your name : ')

while name != "quit":
    print(f"Hello {name}")
    name = input("Enter your name : ")

# so here we use name two times lengthy expression

# ?insted of that i can use walrus Operator


while (name := input(("ENter your name : "))) != "quit":
    print(f"Hello {name}")