class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0, 0, 0]

        for num in nums:
            counts[num] += 1

        # pointer for position of nums
        i = 0

        # Loop through each item of counts
        for v in range(len(counts)):
            # Loop through number of counts, adding to nums
            for c in range(counts[v]):
                nums[i] = v
                i += 1


        