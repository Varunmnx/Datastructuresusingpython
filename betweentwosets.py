a= [2,4]
b=[24,36]

maxA = max(a)
minB = min(b)
count = 0
for i in range(maxA,minB+1):
         val1 = all(i%elem==0 for elem in a)
         val2 = all(elem2%i==0 for elem2 in b)
         count += val1 *val2
print(count)       
