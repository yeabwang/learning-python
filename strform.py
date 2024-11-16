# We can format our strings using the following methods

word = ("Free")

#center 
# In this function we use it to specify the length of our entire string and center our string into it
# To fill the length spaces it will add an extra spaces
# We can specify the separation char
centerWord = word.center(15, "*")
print(centerWord)

#left and right
# This works similar but the alignment will be on the left and on the right side
leftWord = word.ljust(7, "#")
print(leftWord)
rightWord = word.rjust(7,"&")
print(rightWord)

#zfill will fill the un taken places with 0 from the left side
zwords = word.zfill(10) 
print(zwords)