from typing import List

# https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = strs[0]
        for string in strs:
            index = 0
            while ( index < len(lcp) 
                and index < len(string) 
                and string[index] == lcp[index]
            ):
                index = index + 1
            lcp = string[0:index]
        return lcp


sol = Solution()
print(sol.longestCommonPrefix(['flowers', 'flow', 'float']))