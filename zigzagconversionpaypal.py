class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        temp = [[] for i in range(numRows)]

        cnt = 0
        turnBack = False
        for i in s:
            temp[cnt].append(i)
            if turnBack == True:
                if cnt == numRows - 1:
                    turnBack = not turnBack
                    cnt -= 1
                else:
                    cnt += 1
            else:
                if cnt == 0:
                    turnBack = not turnBack
                    cnt += 1
                else:
                    cnt -= 1
        
        retval = ""
        # print(temp)
        for i in temp:
            retval += ''.join(i)
            
        return retval
