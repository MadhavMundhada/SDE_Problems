"""
for i in range(int(input())):
    m,n=map(int,input().split())
    a1=list(map(int,input().split()))
    a2=list(map(int,input().split()))
    i=0
    j=0
    while i<m and j<n:
        if a1[i]<=a2[j]:
            print(a1[i],end=" ")
            i=i+1
        else:
            print(a2[j],end=" ")
            j=j+1
    if i<m:
        while i<m:
            print(a1[i],end=" ")
            i=i+1
    else:
        while j<n:
            print(a2[j],end=" ")
            j=j+1
    print()

	
"""
# Merging two sorted arrays with O(1) 
# extra space 

# Function to find next gap. 
def nextGap( gap): 

	if (gap <= 1): 
		return 0
	return (gap // 2) + (gap % 2) 

def merge(arr1, arr2, n, m): 

	gap = n + m 
	gap = nextGap(gap)
	 
	while gap > 0 : 
		print(gap)
	
		# comparing elements in 
		# the first array. 
		i = 0
		while i + gap < n : 
			if (arr1[i] > arr1[i + gap]): 
				arr1[i], arr1[i + gap] = arr1[i + gap], arr1[i] 
				print(arr1)
				
			i += 1
		

		#comparing elements in both arrays. 
		j = gap - n if gap > n else 0
		while i < n and j < m: 
			if (arr1[i] > arr2[j]): 
				arr1[i], arr2[j] = arr2[j], arr1[i] 
				print(arr1,arr2)
			i += 1
			j += 1

		if (j < m): 
			
			# comparing elements in the 
			# second array. 
			j = 0
			while j + gap < m : 
				if (arr2[j] > arr2[j + gap]): 
					arr2[j], arr2[j + gap] = arr2[j + gap], arr2[j] 
					print(arr2)
				j += 1
				
		gap = nextGap(gap) 

# Driver code 
if __name__ == "__main__": 
	
	a1 = [ 10, 27, 38, 43 ,82 ] 
	a2 = [ 3, 9 ] 
	n = len(a1) 
	m = len(a2) 

	merge(a1, a2, n, m) 

	print("First Array: ", end = "") 
	for i in range(n): 
		print(a1[i], end = " ") 
	print() 

	print("Second Array: ", end = "") 
	for i in range(m): 
		print(a2[i], end = " ") 
	print() 

# This code is contributed 
# by ChitraNayal 
