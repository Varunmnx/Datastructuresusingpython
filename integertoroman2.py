l={
1000:"M"
,900:"CM"
,500:"D"
,400:"CD",
100:"C",
90:"XC"
,50: "L"
,40 : "XL"
,10: "X"
,9: "IX",             
5:"V",      
4:"IV",
1:"I"
}
n =19
s=""
# k=0
for i,j in l.items():
    if n//i:
       k=n//i
       s +=j*k
       n=n%i
print(s)       
