nums = [1,3,6,8,12]
target = 2

# left = 0
# right = len(nums) - 1

# while left <= right:
#     mid = (left + right) // 2
    
#     if nums[mid] == target:
#         print(mid)
#     elif target > nums[mid]:
#         left = mid + 1
#     else:
#         right = mid - 1

# print(left)       


























left = 0 
right = len(nums)-1
mid = 0
while left <=right:
    mid = (left +right)//2
    if  target == nums[mid] :
        print(mid)
    elif  target>nums[mid]:
        left = mid+1
    else:
        right = mid -1
print(left)                 
