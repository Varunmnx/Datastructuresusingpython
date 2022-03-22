nums =[1,2,4,5,6,7,8,9]
k = 3
while k > 0:
            nums.insert(0, nums.pop())
            k -= 1
print(nums)