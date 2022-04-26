n= input()
sum=0
n1=0
n2=1
if n<0:
   print(None)
if n==1 or n==2:
       print(1)
for  i in range(n-1):
   sum =n1+n2
   n1=n2
   n2=sum
print(sum)  