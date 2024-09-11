# Given tested arrays
nums1 = [-4,-1,0,3,10]
nums2 = [-7,-3,2,3,11]

# Return the squared array with the function
def squaresOfArray(arr):
    '''
        Use the map function to square each number in the array
        Use list function so that we can actually see the array in the terminal
        At the very end, use sorted function to sort the array once we have gotten the square of each number
        The lambda method is used as I was unable to create a function inside of leetcode without there being an error
    '''
    return sorted(list(map(lambda x: x * x, arr)))

def main(arr):
    # Grab result and print it
    result = squaresOfArray(arr)
    print(result)

main(nums2)