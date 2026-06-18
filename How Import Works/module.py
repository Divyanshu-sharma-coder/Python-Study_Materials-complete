def moduleloaded():
   print("Module loaded Successfully")


def simpleIntrest():
    try:
     p = int(input("Enter Principle : "))
     r = int(input("ENter rate : "))
     t = int(input("Enter Time : "))
    except ValueError:
       print("Invalid Input")
    return (p*r*t)/100



if(__name__ == "__main__"):
    moduleloaded()