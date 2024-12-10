'''
Exceptions are ways of responding or handling runtime errors gracefully, instead of terminating the program by force.

Key Components
try
Code that might raise an exception is placed inside the try block.

except
Code to handle the exception is written in one or more except blocks.

else
Code in the else block runs if no exceptions occur in the try block.

finally
Code in the finally block runs no matter what, whether an exception occurred or not. This is useful for cleanup actions like closing files.

We can start with the exceptions we already know and work toward to the more generalized exception using Exception class which contains various exceptions.

We can also define our own class of Exception.

'''

try:
    # Code that may raise an exception
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    # Handling specific exception
    print("You cannot divide by zero!")
except Exception as e:
    # Handling another specific exception
    print("Invalid input! Please enter a number.")
else:
    # Runs if no exceptions occur
    print(f"The result is {result}")
finally:
    # Runs no matter what
    print("Execution completed.")
