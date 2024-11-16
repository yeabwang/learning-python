# Here we will try to do a basic string manipulation and see how they appear

fname = "yeabsira"
lname = " Tesfaye"
fullName = fname + lname

# Capitalize the first letter of the first word only
capitalizedName = fullName.capitalize()
print(f"Capitalized: {capitalizedName}")

# lower casing
lowerName = fullName.lower()
print(f"Lower case {lowerName}")

#upper casing
upperName = fullName.upper()
print(f"uppercase: {upperName}")

# Titling will capitalize the first letter of every word
titleName = fullName.title()
print(f"All words start as capital: {titleName}")

#swap casing
swappedName = fullName.swapcase()
print(f"Swapped cased {swappedName}")

#case folding
# Its an aggressive form of lower function, usually implemented when dealing with case insensitive other languages
caseFoldedName = fullName.casefold()
print(f"Case Folded {caseFoldedName}")