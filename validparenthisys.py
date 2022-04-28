s="[]{}()"
stack = []
ss = {"}": "{", "]": "[", ")": "("}
for i in s:
    if i in ss:
        if len(stack)!=0 and i == stack.pop():
            pass
        else:
            print(False)
    else:
        stack.append(i)
if len(stack) ==0:
    print(True)
else:
    print(False)