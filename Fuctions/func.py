# Lambeda Function ----

# def simpleintrest():
#     return (p*r*t)/100

# p = int(input("ENter P ==> "))
# r = int(input("Enter R ==> "))
# t = int(input("Enter T ==> "))

# print(simpleintrest())


# func = lambda p,r,t: (p*r*t)/100
# p = int(input("ENter P ==> "))
# r = int(input("Enter R ==> "))
# t = int(input("Enter T ==> "))
# print(func(p,r,t))


#  map, Filter, Reduce

def square(x):
    return x *  x


li = [2, 3, 4, 5, 6, 7, 8, 9, 10]
# i want a list with square of these all numbers

newli = []
for item in li:
    newli.append(square(item))

print(newli)


#  Using Map
#  so I just do this --
# map(function, iterable)
newli2 = list(map(square, li))
print(newli2)

print()
# Filter : this will filter out our list, tuple etc, a/c to our condition 

# basic way to filter out a list in which element is greater then 5, and less then 10


def filtering(li10, newli10):
   for i in li10:
    if(i >= 4 and i <= 10):
       newli10.append(i)
   return newli10

li2 = [1, 2, 3, 4, 5, 6, 7 ,8, 9, 10, 11, 12, 13, 14, 15]
li3 = []
print(filtering(li2, li3))
print()

# but instead of this i can use filter----
# filter(function , iterable )
newnewli = list(filter(lambda x: 4 <= x <=10, li2))
print(newnewli)

print()


# Reduce fuction ---
# Unlike map and filter it combined all items then give a single answer also we need to import it---

# reduce(Function, iterable)

from functools import reduce

li8 = [2, 4, 6, 8, 10]

sum = reduce(lambda x,y: x+y, li8)
print(sum)

# finding maximum number----

li9 = [32, 64, 45, 98, 9, 43]

max = reduce(lambda x,y: x if x>y else y, li9)
print(max)





















  