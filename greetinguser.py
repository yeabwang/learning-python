# In this program what we will do is we will ask and accept name from the user and greet them by saying hello+name
# Lets now try to divide our so what big problem :) into smaller chunks 

# Prompt the user asking for name -- To do this we can use our print function
# Accept the user name -- to do this we can use another common function input and since input takes an argument, a string which will be used as a prompt we can ignore the first step
# save the user name -- Once the user input their name we need to save it some variable so that we use it later
# concatenate our name with the greeting message -- We need to combine our variable value with our string text
# Or pass the value we get from the name to our function as an argument
# Print out to the console -- Finally print it to the console with print

# Btw, the input function accept as string 
name = input("What is your name? ")
print("Hello, "+name) #Here we have one argument as after concatenation it will be passed as one argument
print("Hello,",name) # Here we have two arguments One thing to note here is if we are passing multi variables it will automatically add the spaces between the arguments
