#backatracking mechanism in python
n=3
result =[]
def parenthisis(left,right,S,n):
    if left == right == n:
        result.append(S)
        return 
    if left<n:
        parenthisis(left+1,right,S+'(',n)
    if right<left:
        parenthisis(left,right+1,S+')',n)
    return result
print(parenthisis(0,0,'',n))            