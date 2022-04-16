class Solution:
    def romanToInt(self, s: str) -> int:
        return self.romanToIntPrivate(s)
    def romanToIntPrivate(self, s: str) -> int:
        singles = dict({
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            })
        result = 0
        for i in reversed(range(len(s))):
            if i < len(s) - 1 and singles[s[i]] < singles[s[i + 1]]:
                continue
            result += singles[s[i]]
            if i > 0 and singles[s[i - 1]] < singles[s[i]]:
                result -= singles[s[i - 1]]
        return result
    
# client
sol = Solution()
print(sol.romanToInt('MCMXCIV'))
