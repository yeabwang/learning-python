name = input("What is your name? ")
age = int(input("How old are you?"))

# Formatted string Literal 
print(f"Hello {name}, You're {age} years old")

# When we are using the formatted literals what we are saying is the things under the curly brace is expression
# Actually as any expression we can do operations on them

print(f"After 20 years you will be {age+20} years old")


# formatting numbers
pi = 3.14159265358979

print(f"The rounded value of pi is {pi: .2f}")