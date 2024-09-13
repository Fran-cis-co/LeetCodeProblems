class Solution(object):
    def isPalindrome(self, s):
        # Create string as arrey for easier viewing, then join everything which is a letter or number
        tempArr = list(s)
        s = ''.join([i for i in s if i.isalpha() or i.isnumeric()])

        # To reverse the string, use reverse slicing and compare the two. I used the lower function to make sure they both have lowecase characters
        return s.lower() == s[::-1].lower()

# --- Test cases --- #
string1 = "A man, a plan, a canal: Panama"
string2 = "race a car"
string3 = " "
string4 = "0P"

# Call function from solution class and print the result (true or false)
sol = Solution()
print(sol.isPalindrome(string4))
