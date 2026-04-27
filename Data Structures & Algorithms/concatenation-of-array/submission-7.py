class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # create an array double the length
        ans = [0] * (2 * len(nums))

        for i in range(len(ans)):
            if 0 <= i < len(nums):
                ans[i] = nums[i]

        for i in range(len(nums)):
            if 0 <= i < len(nums):
                ans[i + len(nums)] = nums[i]

        return ans
