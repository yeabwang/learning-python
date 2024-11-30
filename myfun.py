def main():
    name = input("Whats your name: ")
    hello(name)

# We can give a default value for our parameters
# As long as our function match with the signature, we are good to go

def hello(name="world"):
    print(f"Hello {name}")
    
main()