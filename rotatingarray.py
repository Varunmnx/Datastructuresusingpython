def rotation(key):
    nums =[1,2,3,4,4,5,6,7,8]
    nums[:] = nums[len(nums)-key:] +nums[:len(nums)-key]
    print(nums)

if __name__=="__main__":
    rotation(2)    