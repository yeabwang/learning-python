import random
def main():
    target = random.randint(1, 3)
    guess = getguess()
    if(compare(guess,target)):
        print("Number found")
    else:
        print("Number not found")

def getguess():
    guess = int(input("Whats your guess: "))
    return guess
def compare(guess, target):
    if(guess == target):
        return True
    else:
        return False
    
main()