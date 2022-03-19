class Solution:
    def search(self,nums,target):

        for  i,j in enumerate(nums):
            if j == target:
                return i
    
        return -1
if __name__=="__main__":
    s1 = Solution()
    nums =list(input("enter your numbers").split())    
    target = int(input("enter target"))
    output=s1.search(nums,target)
    print(output)