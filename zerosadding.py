class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
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
            