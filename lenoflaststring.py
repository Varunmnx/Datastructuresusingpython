#length of last string in a list python
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        c=0
        s=s[::-1].strip()
        
        for element in s:
            if element == " ":
                break
                return c 
            else:
                c+=1
        return c        