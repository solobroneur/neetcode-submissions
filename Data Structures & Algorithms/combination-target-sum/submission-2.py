class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # List to contain unique combinations
        output = list()

        # Helper function to do Depth First Search
        def dfs(i, subset, total):
            # Base cases
            ## Found result
            if total == target:
                output.append(subset.copy())
                return
            ## None left or over target
            if i >= len(nums) or total > target:
                return

            current_number = nums[i]

            # Include number into subset
            subset.append(current_number)
            dfs(i, subset, total + current_number)

            # Exclude number from subset
            subset.pop()
            dfs(i + 1, subset, total)

        # Pass in numbers to create a binary tree
        dfs(0, [], 0)

        # Return list of subsets
        return output
