li = [10, 12, 29, 54, 73, 32, 98, 23, 75, 80]
index = 0
for mark in li:
    print(mark, end = " , ")
    if(index == 6):
        print(" mam, You are Awesome....")
    index += 1



li2 = [10, 12, 29, 54, 73, 32, 98, 23, 75, 80]

for index, mark in enumerate(li2):
    print(mark, end = " , ")
    if(index == 6):
        print(" mam You are Awesome")



li3 = ["Apple", "Banana", "PineApple"]
index = 0
for fruit in li3:
    print(fruit, end = " , ")
    print(index)
    print()
    index +=1

li4 =  ["Apple", "Banana", "PineApple"]
for index, fruit in enumerate(li4,):
    print(f"Position : {index} the fruit is {fruit}")

# print(list(enumerate(li4)))



li5 =  ["Apple", "Banana", "PineApple"]
for index, fruit in enumerate(li4, start = 1):
    print(f"Position : {index} the fruit is {fruit}")


a = "Divyanshu"
index = 0
for chars in a :
    print(chars, end = ",")
    print()
    if(index == 4):
        print(f"There is another name in your name and it is {{Divya}}")
    index +=1

b = "Divyanshu"
for index, i in enumerate(b):
    print(i, end =",")
    if(index == 4):
         print(f"There is another name in your name and it is {{Divya}}")



# Real World -Use Case

errors = ["ValueError", "IndexError", "importError", "FileNotFoundError", "IndentationError", "ModuleNotFoundError", "TypeError", "SyntaxError", "KeyError"]

for index, error in enumerate(errors, start=1):
    print(f"Error {index} : {error}")


# result = list(enumerate(errors))
# print(result)






































