from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}
        for idx, value in enumerate(nums):# returns index with value 
            if target - value in values: # this gives both value in the list that should be added to get target
                return [values[target - value], idx]
            else:
                values[value] = idx