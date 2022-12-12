
# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        parens = dict({
            '(': ')',
            '[': ']',
            '{': '}',
        })

        encounteredStack = []
        for i in range(len(s)):
            if s[i] in parens:
                encounteredStack.append(s[i])
                continue
            # s[i] is a closer
            if len(encounteredStack) == 0:
                # no valid opener match
                return False
            previousOpener = encounteredStack[len(encounteredStack) - 1]
            if s[i] != parens[previousOpener]:
                # opener-closer mismatch
                return False
            # valid opener-closer match
            encounteredStack.pop()
        return len(encounteredStack) == 0
            
sol = Solution()
print(sol.isValid(')'))