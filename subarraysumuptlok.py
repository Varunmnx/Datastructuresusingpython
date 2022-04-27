
s=[1,2,3,4,5]
k=5
d={0:1}
anw=0
sp=0
for i in s:
    sp+= i
    diff = sp-k
    if diff in d:
        anw+=1
    d[sp] = d.get(sp,0)+1
print(anw)     