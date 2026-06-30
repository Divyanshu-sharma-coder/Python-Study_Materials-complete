import threading 
import time
# def func():
#     time.sleep(4)
#     print("Slept for 4 seconds ")

def func2():
    time.sleep(5)
    print("Slept for 5 seconds ")

def func3():
    time.sleep(3)
    print("Slept for 3 seconds ")
    
# time1 = time.perf_counter()
# func()
# func2()
# func3()
# time2= time.perf_counter()
# print(f"total time to finish this program is {time2 - time1} seconds")

def func(seconds):
    time.sleep(seconds)
    print(f"The fuction runs for {seconds} second")
time1 = time.perf_counter()
t1 = threading.Thread(target=func, args=[4])
t2 = threading.Thread(target=func, args=[5])
t3 = threading.Thread(target=func, args=[3])

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()
time2= time.perf_counter()
print(f"total time to finish this program is {time2 - time1} seconds")