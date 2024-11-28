status = ""
is_started = False

while True:
    status = input("> ").lower()
    if status == "start":
        if is_started:
            print("The car is already started.. What are you doing?")
        else:
            print("Car started...Ready to go!")
            is_started = True
    elif status == "stop":
        if not is_started:
            print("The car is already stopped. Start before you stop.")
        else:
            print("Car stopped.")
            is_started = False
    elif status == "help":
        print('''Start - to start the car
Stop - to stop the car
quit - to exit
help for help''')
    elif status == "quit":
        break
    else:
        print("I don't understand that...")
