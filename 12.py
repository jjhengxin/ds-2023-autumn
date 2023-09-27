arr=list(map(int,input().split()))
def insertionSort(arr): 
    for i in range(1, len(arr)): 
        q = arr[i] 
        j = i-1
        while j >=0 and q < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = q 
  
insertionSort(arr) 
print ("排序后的数组:",arr) 
