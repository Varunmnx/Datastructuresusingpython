import operator

elements =[1,1,1,1,1,1,1,2,3,4,5,6,6,6,6,6,6,1,2]
repeaters={}
for elem in elements:
    # repeaters[f"{elem}"] = repeaters.get(elem,0)+1
    repeaters[elem] = repeaters.get(elem,0)+1

print(repeaters)
marklist=[(value,key) for (key,value) in repeaters.items()]
print("before sorting the list")
print(marklist)
print("after sorting the list")
sortedset=sorted(marklist) # sorts depending on the first element in the array 
print(sortedset)
print("changing back to dictionary")
rearranged = dict( (k,v) for v,k in  sortedset)
# print (rearranged)
# sorrearranged = sorted(rearranged)
print(rearranged)
