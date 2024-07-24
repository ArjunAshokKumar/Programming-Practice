class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        str_x = str(x)
        x_len = len(str_x)
        for i in range(int(x_len/2)):
            if str_x[i] != str_x[x_len-1-i]:
                return False
        return True

        
obj = Solution()
if obj.isPalindrome(-121):
    print("Is a palindrome.")
else:
    print("Isn't a palindrome.")
