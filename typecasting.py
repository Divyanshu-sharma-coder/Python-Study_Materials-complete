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