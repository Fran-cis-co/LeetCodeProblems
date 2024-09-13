# Import numpy to use prod() function
import numpy as num 

class Solution(object):
    def productExceptSelf(self, nums):
        newArray = []
        '''
        Iterate through given num array and pop the current iterated index to not include it in the product.
        Once we do that, then the prod() function is used from numpy to get the product of the elements in the array.
        This is then added to a new list
        '''
        for i in range(len(nums)):
            tempList = nums[:]
            tempList.pop(i)
            product = int(num.prod(tempList))
            newArray.append(product)
        return newArray

# --- Test Cases --- #
nums1 = [1,2,3, 4]
nums2 = [-1,1,0,-3,3]

# Call method through class reference and print the returning result
sol = Solution()
print(sol.productExceptSelf(nums1))
