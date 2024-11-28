import random
luckyNumber = random.randint(1,10)
numberOfTrials = 3
trialCount = 0

while trialCount < numberOfTrials:
    guess = int(input("Guess the number: "))
    if(guess == luckyNumber):
        print(f"Wow! You got the lucky number, {luckyNumber} in {numberOfTrials} number of trials")
        break
    else:
        print(f"Your guess {guess} is wrong, try again.")
    trialCount +=1
else:
    print(f"The lucky number was {luckyNumber}")       