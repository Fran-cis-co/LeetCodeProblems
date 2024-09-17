class Solution(object):
    def sortArrayByParityII(self,nums):
        # Have arrays where we store the even and odd numbers seperately
        even = []
        odd = []
        result = []

        for i in nums:
            # If the mod of i with 2 is 0, it means it is even which goes into the even array. Else, append in odd array
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)

        '''
        iterate through the range of len(nums) to act as a way to fill the result array
        Use similar method as seperating the odds and evens where we input back an odd or even number
        Pop the numbers from the even and odd arrays until both are empty
        '''
        for i in range(len(nums)):
            if i % 2 == 0:
                if even:
                    result.append(even.pop())
            else:
                if odd:
                    result.append(odd.pop())

        return result

# --- Test Cases --- #
nums1 = [4, 2, 5, 7]
nums2 = [2, 3]


sol = Solution()
print(sol.sortArrayByParityII(nums1))
