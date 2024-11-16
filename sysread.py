# sys.stdin.read()
# We use this function when we want to read the entire thing written in the console or from file till it reaches to EOF
# In console we can indicate the end of the line by hitting ctrl +z
# In a file it automatically reaches to the EOF by itself -- We will see this later
# Once the EOF is encountered:

# The sys.stdin.read() function returns the input received so far as a single string.
# If no input is provided before hitting EOF, it will return an empty string. 

import sys

print("Enter your message: Hit ctrl+z to send")
userInput = sys.stdin.read()
print(f"Your message is {userInput}.")
