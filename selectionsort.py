def main():
    arr = [1,5,2,1,3,4,8,9,1]
    print(selectionSort(arr))

def selectionSort(arr):
    size = len(arr)
    
    for i in range(size-1):
        minIndex = i
        for j in range(minIndex+1, size):
            if(arr[j]<arr[minIndex]):
                minIndex = j
        
        if(i != minIndex):
            arr[i], arr[minIndex] = arr[minIndex], arr[i]
            
    return arr   
main()