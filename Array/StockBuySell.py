"""O(n)"""
arr = list(map(int,input().split()))
minPrice=9999999
maxPro=0
n=len(arr)

for i in range(n):
    minPrice=min(minPrice,arr[i])
    maxPro=max(maxPro,arr[i]-minPrice)
    
print(maxPro)

"""
O(n^2)

arr = list(map(int,input().split()))
mini=arr[0]
pro=0
n=len(arr)

for i in range(1,n-1):
    mini=min(mini,arr[i])
    for j in range(i,n):
        p=arr[j]-mini
        pro=max(pro,p)

print(pro)

7 1 5 3 6 4
"""