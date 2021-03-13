
def duplicates(arr, n): 
	
	for i in range(0, n): 
		index = arr[i] % n 
		arr[index] += n 
		print(arr)

	flag=False

	for i in range(0,n): 
		if (arr[i]//n) > 1: 
			#res.append(i)
			flag=True
			print(i , end = " ") 
	if flag==False:
		print(-1)



"""	    
def duplicates(numRay,arr_size):
	

	for i in range(arr_size):
	


		if numRay[numRay[i] % arr_size] >=arr_size and numRay[numRay[i] % arr_size] <2*arr_size:


			print(numRay[i] % arr_size,end=" ")

		numRay[numRay[i] % arr_size] = numRay[numRay[i] % arr_size] +arr_size; 


"""


if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        duplicates(arr,n)
  


	

