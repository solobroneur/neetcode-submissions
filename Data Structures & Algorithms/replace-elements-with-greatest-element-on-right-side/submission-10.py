# 3. Find the redundancy
# What repeated work is the brute force doing?
# What scans, recalculations, or nested loops are wasteful?

# 4. Eliminate the redundancy
# Use the constraints to guide the right data structure.
# Reason into the solution instead of recalling patterns from memory.

# 5. Decide containers and types
# What needs to be stored?
# Choose the data structure and value types before coding.

# 6. Write the code piece by piece
# Build one section at a time.
# Don't write the entire solution all at once.

# 7. Fix bugs by understanding
# Every bug needs an explanation.
# Understand why it broke before changing the code.


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        output = list()

        for i in range(len(arr)):
            maximum = -1
            for j in range(i + 1, len(arr)):
                if arr[j] > maximum:
                    maximum = arr[j]
                if j == len(arr):
                    maximum = -1
            output.append(maximum)


        return output