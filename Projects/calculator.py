# Calculator


def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mult(a,b):
    return a*b

def div(a,b):
   try:
      return a/b
   except ZeroDivisionError:
      print("Divison by zero is Infinity")

    
def rem(a,b):
    return a%b


while True:
 op = str(input("Enter The Operation : "))
 try: 
   a = int(input("Enter your number : "))
   b = int(input("enter Another Number : "))

 except:
   print("Invalid input please enter a valid input")
   continue

 if(op == "+"):
     print(add(a,b))
 elif(op == "-"):
     print(sub(a,b))
 elif   (op == "*" or op == "x"):
    print(mult(a,b))
 elif(op == "/"):
     print(div(a,b))
 elif (op == "%"):
     print(rem(a,b))
 else:
     print("Enter valid Operation")
