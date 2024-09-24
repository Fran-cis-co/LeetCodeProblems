class Solution(object):
    def shuffle(self, nums, n):
        result = []
        # Slice the original array in half since we know the array consists of size 2n and the x's are first and y's second
        x = nums[0:n]
        y = nums[n:2 * n]
        
        # Utilize count = 0 that way we can grab values from both the x and y arrays 
        count = 0
        while count < n:
            # append popped values into result array that way we can represent the shuffled array: x_n, y_n
            result.append(x[count])
            result.append(y[count])
            count += 1
        
        return result
        


# --- Test Cases --- 
nums1= [2,5,1,3,4,7]
n1 = 3
nums2 = [1,2,3,4,4,3,2,1]
n2 = 4
nums3 = [1,1,2,2]
n3 = 2


sol = Solution()
print(sol.shuffle(nums1, n1))