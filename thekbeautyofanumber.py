class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        
          s,count =0,0
          num =str(num)
          for i in range(len(num)-k+1):
                temp =num[i:i+k]
                if int(temp)!=0 and int(num)%int(temp)==0:
                    count+=1
          return count          