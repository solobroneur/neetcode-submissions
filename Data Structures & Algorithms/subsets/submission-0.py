class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
       # Setup array to track subsets
       output = list()
       # Setup subset to track each option
       subset = list()

       # create function to process recursion
       def dfs(idx):
            # Base case
            # Have you made it all the way through the list of numbers
            if idx >= len(nums):
                # Add the result to the returned array
                output.append(subset.copy())
                return

            # recurse into left decision tree (include)
            subset.append(nums[idx])
            dfs(idx + 1)

            # backtrack (don't include)
            subset.pop()
            dfs(idx + 1)


       # initiate recursion
       dfs(0)

       # return result 
       return output
        