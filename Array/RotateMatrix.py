matrix=[]
for i in range(3):          # A for loop for row entries 
    a=list(map(int,input().split()))
    matrix.append(a)
n=len(matrix)
print("Original",matrix)
for i in range(n):
    for j in range(i):
        matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
print("Transpose",matrix) 
     
for i in range(n):
    matrix[i]=matrix[i][::-1]

print("Rotated",matrix)