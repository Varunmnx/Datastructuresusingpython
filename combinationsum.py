def combinationSum(nums,t):
        res=[]
        helper(res,nums,t,[])
        return res
def helper(res,nums,t,path):
        if t==0:
            res.append(path)
        for i in range(len(nums)):
            if nums[i]>t:
                continue
            helper(res,nums[i:],t-nums[i],path+[nums[i]])

if __name__=="__main__":
    print(combinationSum([1,2,3,4,2],5))
