status = "NULL"

while(status != "quit"):
    status = input("> ").lower()
    if(status == "start"):
        print("Car started...Ready to go!")
    elif(status == "stop"):
        print("Car stopped.")
    elif(status == "help"):
        print('''Start - to start the car \n Stop - to stop the car \n quit - to exit \n help for help ''')
    elif(status == "quit"):
        break
    else:
        print("I don't understand that...")