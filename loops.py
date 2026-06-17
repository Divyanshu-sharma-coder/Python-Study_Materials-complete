# for i in range(0,21, 10):
#     print(i)

#     # (start, end, step)



# # list = ["Yellow", "Green", "Red", "Black", "Voilet"]
# # for li in list:
# #     print(li, end = " : ")
# #     for i in li:
# #         print(i, end = " , ")
# #     print()

# Multiplication Table

x = int(input("Enter a Number for its Multipication Table : "))
for i in range(1,11):
    print(f"{x} X {i} = {x*i}")
    
print()
# While LOOP
y = int(input("Enter another Number : "))
j = 1
while(j <= 10):
     print(f"{y} X {j} = {y*j}")
     j += 1
print()

# Reverse table
z = int(input("Enter another Number : "))
k = 10
while(k >= 1):
     print(f"{z} X {k} = {z*k}")
     k -= 1
print()

# Using For Loop


r = int(input("Enter a Number for its Multipication Table : "))

for i in range(10,0, -1):
     print(f"{r} X {i} = {r*i}")
    #  i -= 1