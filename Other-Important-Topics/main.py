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


