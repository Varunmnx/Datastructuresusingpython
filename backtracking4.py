from turtle import back


result=[]
n=3
def backtracking(start,end,S,result):
    if start == end ==n:
        result.append(S)
        return result
    if start<end:
        result = backtracking(start+1,end,S+"(",result)
    if end<start:
        result = backtracking(start,end+1,S+")",result)
    return result        
print(backtracking(0,0,'',result))            