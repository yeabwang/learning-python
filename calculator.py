x = float(input("Whats the value of x: "))
y = float(input("Whats the value of y: "))

# Rounding numbers
# Currently the limit on int numbers is removed so they can be as big as we want them to be 
s = round(x+y,2)
d = x/y

# :, - This will do a good formatting by separating every thousand values by a comma 
print(f"The addition answer is {s:,}")
print(f"The division answer is {d:.2f}")