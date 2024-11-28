# x = 2088888
# print("%x" %x)
# for i in range(1,5,2):
#     print(i)

# fruit = ["Apple","Bababa", "See"]
# color = ["Red", "Blue", "White"]

# for x,y in zip(fruit,color):
#     print(x, "is", y)

# some more functions
def is_prime(n):
    if n in [2, 3]:
        return True
    if (n == 1) or (n % 2 == 0):
        return False
    r = 4
    while r * r <= n:
        if n % r == 0:
            return False
        r += 2
    return True
print(is_prime(78), is_prime(79))
    
# def variable():
#     global x
#     x = 10
#     x += 5 
#     print(f"Inside Scope {x}")
    
# variable()
# print(f"Out of scope {x}")
# text = "Hello, Python! "
# print(text.index('e'))