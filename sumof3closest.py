class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        clo = 5000
        
        for i in range(0,len(nums)-2):
              first =i+1
              last = len(nums)-1  
              while first<last:
                    sumof3 = nums[i] + nums[first]+nums[last]
                    if sumof3 == target:
                        return target
                    if abs(target-sumof3)< abs(target-clo):
                         clo = sumof3
                         # print(clo)   
                    if sumof3<=target:
                         first+=1             
                    else:
                         last-=1
                        
        return clo             
                