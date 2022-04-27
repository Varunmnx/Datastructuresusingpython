count =0
s=[1,2,3,4,5]
k=1
sum=0
hashmap ={0:1}
for i in s:
    sum +=i   
    for key,item in hashmap.items():
        if (sum-key)%k ==0:
            count +=1


    hashmap[sum] = hashmap.get(sum,0)+1    
print(count)