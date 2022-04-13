#i like the green
d= set()
l=0 # length of eachstring
s ="abcdefabcabcdefg" # l will be at beginning
res = 0
for i in range(len(s)):
     while s[i] in d:
         d.remove(s[i])
         l+=1
     d.add(s[i])
    #  res = max(res,i-l+1)
     if res< l:
         res = i-l+1              
print(res)
         
