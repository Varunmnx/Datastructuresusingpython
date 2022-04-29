result =[]
combinations=[]
n=3
def backtracking(leftcount,rightcount):
    if leftcount ==rightcount ==n:
        result.append(''.join(combinations))
    if leftcount < n:
        combinations.append("(")
        backtracking(leftcount+1,rightcount)
        combinations.pop()
    if rightcount <leftcount:
        combinations.append(")")
        backtracking(leftcount,rightcount+1)
        combinations.pop()
backtracking(0,0)
print(result)