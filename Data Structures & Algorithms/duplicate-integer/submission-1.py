class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        values = {}
        for num in nums:
            if num not in values:
                values[num] = 1
            else:
                return True
        
        return False

        