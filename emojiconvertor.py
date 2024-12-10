def main():
    myinput = input("> ").split(" ")
    print(emojiConvertor(myinput))  
        
def dataset(value):
    emojies = {
    ":)" : "😁",
    "(:" : "😭",
    "*)" : "😱",
    "#(" : "😡"    
    }
    
    if emojies.get(value) != None:
        return emojies.get(value)
    else:
        return value
    
def emojiConvertor(text):
    output = ""
    for char in text:
        output += dataset(char) + " "   
    return output  
    
main()
