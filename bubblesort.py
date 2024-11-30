def main():
    array = [3,1,6,22,6,90,1]
    sortedArray = bubbleSort(array)
    
    print(sortedArray)

def bubbleSort(array):
    
    is_swapped = False 
    for k in range(len(array)-1):
        for i in range((len(array)-1)-k):
            if(array[i] > array[i+1]):
                temp = array[i]
                array[i] = array[i+1]
                array[i+1] = temp
                is_swapped = True
    
        if(not is_swapped):
            break     
    return array


main()