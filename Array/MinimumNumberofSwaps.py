arr=list(map(int,input().split()))

# map the indexes of the current elements
indexes = {e: i for i, e in enumerate(arr)}
print(indexes)
# keep track of the swaps
swaps = 0
for i, e in enumerate(arr):
    # where is the number that should be here?
    print(i,e)
    where = indexes[i+1]
    # number already sorted, skip
    if arr[where] == arr[i]: continue
    # swap
    arr[where], arr[i] = arr[i], arr[where]
    swaps += 1
    print(arr)
    # update map of indexes
    indexes[e] = indexes[i+1]
    print(indexes)
print(swaps) 


