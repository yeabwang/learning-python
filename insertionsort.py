def main():
    arr = [5,3,2,16,3,2]
    print(insertionSort(arr))
    
def insertionSort(arr):
    size = len(arr)
    
    for i in range(1,size):
        anchor = arr[i] 
        j = i-1
        
        while j>=0 and anchor < arr[j]:
            arr[j+1] = arr[j]
            j-=1
            
        arr[j+1] = anchor
    
    return arr
        
main()