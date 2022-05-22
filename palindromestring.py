class Solution:
	def longestPalindrome(self, s: str) -> str:
	         res =""
             Rlen = 0
        
             for i in range(len(s)):
             #for finding odd string palindrom
                  l,r=i,i
                  while l>=0 and r<len(s) and s[l]==s[r]:
                        if (r-l+1) >Rlen:
                             res = s[l:r+1] #removes the l elements from the beginning an
                             Rlen = r-l+1
                        #have to execute this anyway
                        l-=1
                        r+=1
                  #for finding the even sum palindrom
                  l,r=i,i+1
                  while l>=0 and r<len(s) and s[l]==s[r]:
                         if (r-l+1) >Rlen:
                                res = s[l:r+1] #removes the l elements from the beginning an
                                Rlen = r-l+1
                         #have to execute this anyway
                         l-=1
                         r+=1
             return res        