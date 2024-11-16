#This is used for securely accepting passwords or sensitive input. 
#The input is hidden (not displayed as the user types).

import getpass
password = getpass.getpass("Enter your password: ")
print("Password received.")
print(f"Your password is {password}")