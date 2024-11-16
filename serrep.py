# These are methods we can use in our functions 

# Find 
# What this function does is it will search the requested chart and if it founds it, will return the index of the first appearance
# If its not found, it will return -1

words = "Hello, My name is Yeabsira Tesfaye and I am a beast. and another is for counting"
statFound = int(words.find("I"))
statNFound = int(words.find("Dumb"))

print(statFound) # Return the index 
print(statNFound) # return -1


# Index
# This is similar to find but index will check value errors not only type errors
# Value errors are errors that happen when the type of the data is correct but the expected value is not.
# Type error is when there is a type mismatch

indexFound = int(words.index("My"))
# indexNFound = int(words.index("Go")) -- This will give us a value error

print(indexFound) # Return the index 


#rfind 
# This is similar to the find but it returns the index of the last occurrence 

rindexFound = int(words.rindex("I"))
#rindexNFound = int(words.rindex("Dumb"))

print(rindexFound) # Return the index 
print(rindexFound) # return -1

#replace
# This replaces all the occurrences and change it with the new one
newString = words.replace("I", "He").replace("am", "is")
print(newString)

#count
# This counts the number of occurrences of the search key in the given string
wordcount = words.count("is")
print(wordcount)