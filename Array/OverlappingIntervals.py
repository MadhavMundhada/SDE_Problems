
# Python3 program to merge overlapping Intervals 
# in O(n Log n) time and O(1) extra space 
"""
def mergeIntervals(arr): 
		
		# Sorting based on the increasing order 
		# of the start intervals 
		arr.sort(key = lambda x: x[0]) 
		
		# array to hold the merged intervals 
		m = [] 
		s = -10000
		max = -100000
		for i in range(len(arr)): 
			a = arr[i] 
			if a[0] > max: 
				if i != 0: 
					m.append([s,max]) 
				max = a[1] 
				s = a[0] 
			else: 
				if a[1] >= max: 
					max = a[1] 
		
		#'max' value gives the last point of 
		# that particular interval 
		# 's' gives the starting point of that interval 
		# 'm' array contains the list of all merged intervals 

		if max != -100000 and [s, max] not in m: 
			m.append([s, max]) 
		#print("The Merged Intervals are :", end = " ") 
		for i in range(len(m)): 
			print(*m[i], end = " ") 

# Driver code 
m=int(input())
for i in range(m):
    n=int(input())
        
    arr = [int(x) for x in input().split()]
    arr = [arr[i:i+2] for i in range(0, n*2, 2)]
    #print(sorted(arr))

    mergeIntervals(arr) 
    print()

# This code is contributed 
# by thirumalai srinivasan 
"""
t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr = [arr[i:i+2] for i in range(0, n*2, 2)]
	
    arr = sorted(arr, key=lambda x: x[0])
    print(arr)
    i = 1
    while i < len(arr):
        if arr[i][0] <= arr[i-1][1]:
            arr[i-1][0] = min(arr[i][0],arr[i-1][0])
            arr[i-1][1] = max(arr[i][1],arr[i-1][1])
            
            print(arr.pop(i))
            print(arr)
        else:
            i+=1
    for a in arr:
        print(a[0],a[1],end=" ")
    print()
    print(arr)
	