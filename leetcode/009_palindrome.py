# https://leetcode.com/problems/palindrome-number/
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return self.isPalindromeNoStringConvert(x)
    def isPalindromeConvertToString(self, x: int) -> bool:
        s = str(x)
        strlen = len(s)
        for i, c in enumerate(s):
            if c != s[strlen - 1 - i]:
                return False
        # no mismatches
        return True
    def isPalindromeNoStringConvert(self, x: int) -> bool:
        y = 0
        orig = x
        while x > 0:
            y = (int(y * 10)) + (int(x % 10))
            x = int(x / 10)
        if y == orig:
            return True
        return False


sol = Solution()
print(sol.isPalindrome(127343721))