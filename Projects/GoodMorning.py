import time

timestamp = time.strftime("%H:%M:%S")
print(timestamp)

if(timestamp >= "06:00:00" and timestamp < "12:00:00"):
    print("Good Morning Sir 🫡🫡")

elif(timestamp >= "12:00:00" and timestamp < "17:00:00"):
    print("Good AfterNoon Sir 😎😎")
elif(timestamp >= "17:00:00" and timestamp < "20:00:00"):
    print("Good Evening sir 🫠🫠")
else:
    print("Good Night Sir 😴😴")

