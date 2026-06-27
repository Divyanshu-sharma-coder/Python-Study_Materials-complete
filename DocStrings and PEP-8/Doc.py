def simpleintrest(p,r,t):
    """This is a Docstring and this function is used to Finds out Simple Intrest"""
    return (p*r*t)/100

# p = int(input("Enter Principle : "))
# r = int(input("Enter rate : "))
# t = int(input("Enter time " ))

result = simpleintrest(p=50,r=50,t=10)
print(result)
print(simpleintrest.__doc__)





def square(n):
    print(n)
    """Takes in a number n and returns its square."""
    print(n ** 2)

print(square.__doc__)

# Output:
# None

