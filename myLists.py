myList = [2,30,6,1,9,10,2,3,2]

print(sorted(myList)[-1])
max = myList[0]
for i in myList:
    if(i > max):
        max = i 
print(max)

for x,y in enumerate(myList):
    print(x,y)
    
myset = set(myList)
print(myset)