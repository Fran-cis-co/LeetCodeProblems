class Solution(object):
    def removeKdigits(self, num, k):
        arr = []
        numString = list(str(num))
        
        for i in range(len(numString) - 3):
            tempString = numString[:]
            arr.append(int(''.join(tempString)))
        return arr
        
        

# --- Test Cases --- #
cases = [[1432219, 3], [10200, 1], [10, 2]]

test = str(1432219)

sol = Solution()

# Iterate through test cases and print result of each
# for i, j in cases:
#     result = sol.removeKdigits(i, j)
#     print(result)

print(sol.removeKdigits(cases[0][0], cases[0][1]))