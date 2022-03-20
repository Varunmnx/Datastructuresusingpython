from multiprocessing.sharedctypes import Value


class Solution:
	def isBadVersion(mid):
           pass
    
def firstBadVersion(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		left = 1
		right = n
    
		while left <= right:
			mid = int((left + right) / 2)
        
			if self.isBadVersion(mid):
				if not self.isBadVersion(mid - 1):
					return mid
				else:
					right = mid - 1
			else:
				left = mid + 1

























                # left =1 
                # right = n
                # mid = 0
                # while left<right :
                #     mid = (left +right )//2
                #     if value == arr[mid]:
                #         if not value == arr[mid-1]:
                #             return mid
                #         else:
                #             return right = mid -1    
                #     else:
                #         return right = mid+1
                # left = 1
                # right = len(array)
                # mid = 0
                # while left<right :
                #     mid = left +right   
                #     if value == arr[mid]:
                #         if not value == arr[mid-1]:
                #             return mid 
                #         else :
                #             return right = mid-1                                
                #     else:
                #         return right = mid+1
                # left = 1
                # right = n
                # mid =0
                # while left <right :
                #     mid = (left +right) //2
                #     if value == arr[mid]:
                #         if not value ==arr[mid-1] :
                #             return mid 
                #         else:
                #             return left = mid -1
                #     else:
                #         return left = mid +1
