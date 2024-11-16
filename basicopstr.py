# We can do basic operations in c as concatenation, repetition, accessing individual elements and slicing it

fname = "Yeabsira "
lname = "Tesfaye"

# concatenation
fulname = fname + lname
print(f"The full name is: {fulname}")
# Repeating the name 3 times
repeatedname = fname * 3
print(f"The repeated names are: {repeatedname}")
# Accessing the first letter from the name
firstchar = fname[0]
print(f"The first char is {firstchar}")
# creating a slice from our string but here it doesn't account the last number so we will be expecting the 2nd and 3rd element here
slicedname = fname[2:4]
print(f"The sliced name is {slicedname}")
