expenses = [2200,2350,2600,2130,2190]

# Compare jan and feb and get the extra amount you expend
extra = expenses[1] - expenses[0]
print(f"The extra amount you spent is {extra}")

#Find out the first quarter expense
sizeofQuarter = 0
total = 0
while sizeofQuarter < 3:
    total += expenses[sizeofQuarter]
    sizeofQuarter +=1
print(f"The Total amount you spent in the fist quarter is {total}")

# Find if you have spent exactly 2000 USD
for money in expenses:
    if(money == 2200):
        print("Yes")
print(2000 in expenses)
expenses.append(1980)
print(expenses)
expenses[3] -= 200 
print(expenses)
