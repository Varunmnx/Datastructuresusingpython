n = 2
trust = [[1,2]]
matrix =[0]*(n+1)
for first,second in trust:
    matrix[first] -= 1
    matrix[second] +=1
for i in range(1,n+1):
    if matrix[i] ==n-1:
        print(i)
print(-1)        