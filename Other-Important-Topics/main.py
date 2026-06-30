#  Wa;rus Operator 

# # so why we need it because -----
# # if i want to erite this expression

# name = input('Enter your name : ')

# while name != "quit":
#     print(f"Hello {name}")
#     name = input("Enter your name : ")

# # so here we use name two times lengthy expression

# # ?insted of that i can use walrus Operator


# while (name := input(("ENter your name : "))) != "quit":
#     print(f"Hello {name}")


print(" --------------------------------Generators-------------------------------------")
# Generators are Generators are a special type of function in Python that produce values one at a time instead of storing everything in memory.

# They behave like iterators but are much more memory efficient.
class my_generator:
    def ge(self):
        for i in range(100):
            yield i

gen = my_generator()
# Create the generator object once
generator_instance = gen.ge()

# Use next() to retrieve values one by one from the same instance
print(next(generator_instance)) # 0
print(next(generator_instance)) # 1
print(next(generator_instance)) # 2   

print()
print('----------------------------Function Caching-------------------------------------')
# Function caching is an optimization technique used to store results of expensive function calls so that future calls with the same inputs can be served instantly.

# This avoids:

# Re-computation
# Unnecessary CPU usage
# Repeated delays

import functools
import time

@functools.lru_cache(maxsize=None)
def expensive_calculation(n):
    print(f"Computing calculation for {n}...")
    time.sleep(5)  # Simulating heavy computation
    return n * 2


# First run (no cache)
print(expensive_calculation(20))
print(expensive_calculation(2))
print(expensive_calculation(6))

print("-" * 20)

# Second run (cached values)
print(expensive_calculation(20))
print(expensive_calculation(2))
print(expensive_calculation(6))

print("-" * 20)

# New value (not cached)
print(expensive_calculation(61))


import sys

# 1. Define the generator function
def log_filter_generator(file_path, keyword):
    """Yields lines from a file one-by-one only if they contain the keyword."""
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if keyword in line:
                # The yield keyword pauses the function and returns data one drop at a time
                yield line.strip() 

# 2. Use the generator in a program
if __name__ == "__main__":
    # Pretend server_logs.txt is a massive 10GB file
    log_file = "server_logs.txt"
    search_term = "ERROR"
    
    # Initialize the generator object (No data is read or stored yet!)
    error_stream = log_filter_generator(log_file, search_term)
    
    print(f"Memory size of generator object: {sys.getsizeof(error_stream)} bytes\n")
    print("Streaming matching logs:")
    
    # Loop over the generator to consume values lazily on-demand
    for error_log in error_stream:
        print(f"-> {error_log}")

