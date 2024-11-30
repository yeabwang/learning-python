# As every language learning process we will start our journey by writing the famous helloworld program
# In this program we will be using one in built function to print out to console
# The effect we see which can be visual or other effects as a part of our function are called side effects

# print("Hello, world!")  

# Arguments are an input to the function affecting the behavior of the function
# When we talk about what the functions can take, we say those are parameters
    # We have two types of parameters:
        #Positional Parameter - These are parameters that work by the order.
        # Named Parameter - These are parameter we provide the key for the values we are going to pass.
# Side effects are any observable change in the state of a program on its environment made by the execution of the code /
# Return values, these are values that are handed back from the functions

# name = input("Whats your name? ")
# print("Hello " + name +"!") # String concatination 
# print(f"Hello {name}!") #String format
# print("Hello ", format(name), "!", sep="")
# print("Hello ", end="")
# print(name)

# We can strip the user input

name = input("Whats your name: ")
print(f"Hello {name.strip().title()}")
firstName, lastName = name.split()
print(firstName,lastName)