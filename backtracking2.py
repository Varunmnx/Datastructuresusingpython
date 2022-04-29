result = []
paren = []
n =3

def backTrack(leftCount, rightCount):
    if leftCount > n:
        return

    if rightCount > leftCount:
        return

    if leftCount == rightCount == n:
        result.append("".join(paren))
        # return

    paren.append("(")
    backTrack(leftCount + 1, rightCount)
    paren.pop()

    paren.append(")")
    backTrack(leftCount, rightCount + 1)
    paren.pop()
backTrack(0,0)
print(result)
