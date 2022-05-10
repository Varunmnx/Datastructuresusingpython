nums = [1,0,-1,0,-2,2]  # -2,-1,0,0,1,2
target = 0
result =[]
unique =set()
nums.sort()
n = len(nums)
i=0
for i in range(n-3):
  for j in range(i+1,n-2):
        start = j+1
        end = n-1
        while start <end :
            if nums[i]+nums[start]+nums[j]+nums[end] == target :
                if(nums[i],nums[start],nums[j],nums[end]) not in unique:
                    unique.add((nums[i],nums[start],nums[j],nums[end])) 
                    result.append([nums[i],nums[start],nums[j],nums[end]])
                start+=1
                end -=1
            elif nums[i]+nums[start]+nums[j]+nums[end] < target:
                start+=1
            else:
                end-=1
                
print(result)                   
            