class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # create an array double the length
        n = len(nums)
        ans = [0] * (2 * n)

        for i, num in enumerate(nums):
            if 0 <= i < n:
                ans[i] = num
                ans[i + n] = num

        return ans
