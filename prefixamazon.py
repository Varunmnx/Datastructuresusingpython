strs = ["ello","englisg","enable","england"]
first = strs[0]
prelen = len(first)
for s in strs[1:]:
    while first[0:prelen] != s[0:prelen]:
        first = first[0:prelen-1]
        prelen -= 1
        if prelen ==0:
            print("no common values")
print(first)            
        