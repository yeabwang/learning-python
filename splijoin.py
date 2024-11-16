# There are various of splitting and joining strings 

shoppingList = "apple, banana, egg, water"

#split
# This will separate one string into multiple strings based on the space. If there is no space char provided it will separate it based on any char it founds
splittedList = shoppingList.split(",")
print(splittedList)

#rsplit 
# This split our string starting from the right side 
# We can limit the number of splits we are going to do
rSplittedWords = shoppingList.rsplit(",", 2)
print(rSplittedWords)

#splitlines
# We can use this to split our string into multiple lines string
# This works on new lines as \n 
words = "new\nlines\nis\nseparated"

separatedLines = words.splitlines()
print(separatedLines)