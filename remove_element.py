class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n=len(nums)
        
        if n==1:
            if val==nums[0]:
                return 0
            else:
                return 1
        i=0
        j=n-1
        k=0
        while i<=j:
            
            if nums[j]==val:
                j-=1
                k+=1
            
            elif nums[i]==val and nums[j]!=val:
                nums[i],nums[j]=nums[j],nums[i]
                k+=1
                i+=1
                j-=1
            elif nums[i]!=val and nums[j]!=val:
                i+=1
        
        return n-k
            
        
