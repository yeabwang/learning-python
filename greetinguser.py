# Reading input from the console
# When you use this the input you are getting will be a string so if you are expecting another type you need to cast it
name = input("What is your name?")
print(f"Hello {name}!")

# Handling spaces and capitalization and greeting by first name
name = name.strip().title()
firstName, lastName = name.split(" ")

print(f"Hello {firstName}")
