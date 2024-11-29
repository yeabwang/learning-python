myList = [1,2,3,3,4,5,6]
target = 2

for i in range(myList):
    mid = len(myList)//2
    if(myList[mid] == myList[i]):
        print("We found the number")
    elif(myList[mid] < myList[i]):
        break