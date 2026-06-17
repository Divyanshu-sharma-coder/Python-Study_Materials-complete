def func(a, b):
    average = (a+b)/2
    return average

print(func(10,18))

# above is the example of Required Arguments----

def func2(c=19, d=21):
    average2 = (c+d)/2
    return average2

print(func2())
print(func2(c =5))
print(func2(c=23,d=12))

# This is Default Arguments Example----

def func3(x,y):
    average = (x+y)/2
    return average

print(func3(y=12,x=34))

# This is Keyword Argument in which order dosen't matter

# Variable Length Arguments----
# Arbitary---
# in which we dont give a fix numbers of arguments just pass *args that stored values inside a tuple 
def func4(*args):
    sum = 0
    for i in args:
        sum+=i
    return sum

print(func4(1,2,3,4))

# Kwargs

def build_profile(name, **kwargs):
    print(f"--- Profile for {name} ---")
    
    # kwargs is just a dictionary inside the function
    for key, value in kwargs.items():
        print(f"{key.title()}: {value}")
    
    print("-" * 25)

# User 1: Only provides mandatory name and one extra detail
build_profile("Alice", role="Developer")

# User 2: Provides multiple extra details
build_profile("Bob", role="Designer", city="Jaipur", experience="5 years")
