mylist = [1,3,4,4,5,2]
unique = []
for i in mylist:
    if(i not in unique):
        unique.append(i)
        
print(unique)