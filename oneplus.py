from ast import literal_eval


l=[1,2,4,5]
l= "".join(map(str,l))
# print(l)
l= int(l)
l+=1
l=list(map(int,str(l)))
print(l)