class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        matcher = { 
            "]": "[",
            "}": "{",
            ")": "(",
        }

        # Preconditions
        is_even = len(s) % 2 == 0
        starts_with_closing = s[0] in matcher

        if not is_even or starts_with_closing:
            return False


        for char in s:
            if char in matcher:
                if stack and stack[-1] == matcher[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return True if not stack else False