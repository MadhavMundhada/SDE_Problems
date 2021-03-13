def nextper(arr,i,found):
    while i>=0:

        if arr[i]<arr[i+1]:
            found=True
            break
        i-=1

        if not found:
            arr.sort()
            return arr

        else:
            j=i+1
            while j<n and arr[j]>arr[i]:
                j+=1

            j-=1

            arr[i],arr[j]=arr[j],arr[i]
            arr[i+1:]=arr[i+1][::-1]
            return arr

arr=list(map(int,input().split()))

n=len(arr)
i=n-2
found=False
res=nextper(arr,i,found)
print(res)