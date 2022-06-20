# find the pivot index such that the left sum is equal to right
def pivotindexfinder(arr):
  S = sum(arr)
  leftsum = 0 
  #since at the pivot index the left sum and right sum would be equal just keep track of leftsum 
  for i in range(len(arr)):
        if leftsum == ( S-leftsum-arr[i] ):
             return i
        leftsum += arr[i]
  return -1       
                 
