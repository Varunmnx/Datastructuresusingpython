class Solution:
    def moveZeroes(self, nums) :
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)-1
        r = 0
        for i in nums:
            if i == 0:
                nums.remove(i)
                nums.append(i)
        print(nums)        


if __name__ =="__main__":
    s = Solution()
    nums = [1,2,0,3,40,5,0,0]
    s.moveZeroes(nums)            