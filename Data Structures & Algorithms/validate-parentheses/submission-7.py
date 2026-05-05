class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

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