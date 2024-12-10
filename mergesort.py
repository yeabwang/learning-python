def main():
    arr = [5,1,21,2,1,6,3]
    print(dividing(arr))

def dividing(arr):
    size = len(arr)
    mid = size // 2
    
    if size <= 1:
        return arr
    
    leftHalf = dividing(arr[:mid])
    rightHalf = dividing(arr[mid:])
    
    return merging(leftHalf, rightHalf)

def merging(leftHalf,rightHalf):
    sizeA = len(leftHalf)
    sizeB = len(rightHalf)
    sortedList = []
    
    i = j = 0
    
    while i < sizeA and j < sizeB:
        if(leftHalf[i] <= rightHalf[j]):
            sortedList.append(leftHalf[i])
            i+=1
        else:
            sortedList.append(rightHalf[j])
            j+=1
    sortedList.extend(leftHalf[i:])
    sortedList.extend(rightHalf[j:])
    
    return sortedList
        
main()