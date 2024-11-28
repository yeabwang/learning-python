name = input("What is your name? ")

if(len(name) > 10):
    print("The length exceed the max number of 10 char.")
else:
    print(f"Welcome to our bank {name}!")