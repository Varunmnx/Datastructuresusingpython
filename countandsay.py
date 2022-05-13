n=2
s='1'
ans=""
if n==1: print("1")
for j in range(n-1):
    c,i,l=1,0,len(s)
    while(i<l):
        if i!=l-1 and s[i]==s[i+1]:
            c+=1
        else:
            ans+=str(c)+s[i]
            c=1
        i+=1
    s=ans
    # print(s)
    ans=''
print(s)