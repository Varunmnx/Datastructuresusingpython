# #i like the green
# d= set()
# l=0 # length of eachstring
s ="abcdbcdefgh" 
         
# charset =set()
# l=0
# res = 0
# for r in range(len(s)):
#     while s[r] in charset:
#         charset.remove(s[l])
#         l+=1
#     charset.add(s[r])
#     res =max(res,r-l+1)
# print(res)  
# # print(l)

charset = set()
l=0
res =0
for r in range(len(s)):
    while s[r] in charset:
        charset.remove(s[l])
        l+=1
    charset.add(s[r])
    res= max(res,r-l+1)
print(res)    

      
