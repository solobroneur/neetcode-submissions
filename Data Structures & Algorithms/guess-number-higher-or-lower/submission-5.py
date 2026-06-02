# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:


class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n

        # Loop & halve until number found
        while left <= right:
            # Compute the middle
            middle = (left + right) // 2
            result = guess(middle)

            # Is it too big?
            if result > 0:
                left = middle + 1
            # Is it too small?
            elif result < 0:
                right = middle - 1
            # It's just right
            else:
                return middle

        # Number not found
        return -1
