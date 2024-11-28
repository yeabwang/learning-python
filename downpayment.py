creditScore = int(input("Whats your credit score? "))
housePrice = int(input("Whats the price of the house? "))
goodPercent = 10
badPercent = 20

if((creditScore > 5 and creditScore <10) and housePrice > 0):
    print(f"You have a very good score and you need to pay {goodPercent}% which is {(goodPercent/100)*housePrice} USD")
elif((creditScore <=5 and creditScore > 0) and housePrice > 0):
    print(f"You have a very bad score and you need to pay {badPercent}% which is {(badPercent/100)*housePrice} USD")
else:
    print("Invalid Input.")