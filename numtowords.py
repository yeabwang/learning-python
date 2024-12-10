phones = {
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four"
}

userInput = list((input("Phone: ")))

for num in userInput:
    print(phones.get(int(num), "Number doesn't exits"), end = " ")