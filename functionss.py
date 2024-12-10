def main():
    userinput = input("What is your name: ")
    print(mymess(userinput))

def mymess(name = "World"):
    return (f"Hello {name}")
    
    # We can either use key word or positional arguments, also our function call should match our function signature
    # If we don't have a return statement python by default will return None
    
main()