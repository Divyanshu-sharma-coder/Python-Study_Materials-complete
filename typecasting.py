# Explicit typecasting

a = "5"
b = "7"

print(a + b)

# 57

c = int(a)
d = int(b)

x = c +d
print(type(x))

# Implicit typecasting

a = 2.5
b = 8


y = a*b

print(type(a))
print(type(b))
print(type(y))






lis = [1, 2, 3, 4, 5]
target = 6
index = 0
founded = True
for i in lis:
    if(i == target):
        founded = True
        index2 = index
        break
    else:
        founded = False
    index +=1

if(founded):
     print(f"The Targeted value Founded at {index2}")
else:
     print("Not Founded")





lis = [1, 2, 3, 4, 5]
target = 34

for index, i in enumerate(lis):
    if(i == target):
        founded = True
        index2 = index 
        break
    else:
        founded = False

if(founded):
    print(f"The Targeted value Founded at {index2}")
else:
     print("Not Founded")
























