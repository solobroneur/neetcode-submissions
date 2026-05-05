class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        matcher = { 
            "]": "[",
            "}": "{",
            ")": "(",
        }

        for char in s:
            if char in matcher:
                if stack and stack[-1] == matcher[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return True if not stack else False