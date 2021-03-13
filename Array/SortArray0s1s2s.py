# Python program to sort an array with 0,1 and 2 in a siingle pass 

# Function to sort array 
def DNFS( arr, arr_size):
    
    
    low = 0
    high = arr_size - 1
    mid = 0
    while mid <= high: 
        
        if arr[mid] == 0: 
            
            
            arr[low],arr[mid] = arr[mid],arr[low] 
            low = low + 1
            mid = mid + 1
        elif arr[mid] == 1: 
            mid = mid + 1
        else: 
            arr[mid],arr[high] = arr[high],arr[mid] 
            high = high - 1
        print(*arr) 

    """
    1
    5
    0 2 1 2 0
    0 0 1 2 2
    """
    
    
        
    
    
for i in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    DNFS(arr,n)
