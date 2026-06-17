# x = 10

# # This triggers: SyntaxWarning: "is" with a literal. Did you mean "=="?
# if x is 10:
#     print("Match found!")

try:
 a = int(input("ENter a Number : "))

except ValueError as e:
 print(f"wrong string literal {e}")
