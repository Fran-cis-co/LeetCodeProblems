class Solution(object):
    def findColumnWidth(self, grid):
        # Create result array which we can put in the max width of each column
        result = []
        

        # Use count and go up to how many rows there are in the grid
        count = 0
        while count < len(grid[0]):
            # Go through each column of the grid and determine which digit has the largest width which determines the width of the column
            tempArray = []
            for x in range(len(grid)):
                # Convert to string before finding the length of each digit to make it easier
                tempArray.append(len(str(grid[x][count])))
            # Find the max width of the column and add it to the result array
            result.append(max(tempArray))
            count += 1
        

        return result
            

            

        

# --- Test Cases --- #
grid1 = [[1], [22], [333]]
grid2 = [[-15, 1, 3], [15, 7, 12], [5, 6, -2]]

# create object reference to class and print result from function
sol = Solution()
print(sol.findColumnWidth(grid1))