# Python3 code to Find the repeating 
# and the missing elements

def printTwoElements( arr, size):
	for i in range(size):
		if arr[abs(arr[i])-1] > 0:
			arr[abs(arr[i])-1] = -arr[abs(arr[i])-1]
		else:
			print("The repeating element is", abs(arr[i]))
		print(i,arr)		
	for i in range(size):
		if arr[i]>0:
			print("and the missing element is", i + 1)

# Driver program to test above function */
arr = [1,2,2,5,4,4]
n = len(arr)
printTwoElements(arr, n)

# This code is contributed by "Abhishek Sharma 44"
