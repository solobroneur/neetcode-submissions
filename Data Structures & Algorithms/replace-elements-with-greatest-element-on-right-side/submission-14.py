class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rightMaximum = -1

        for i in range(len(arr) - 1, -1, -1):
            newMaximum = max(rightMaximum, arr[i])
            arr[i] = rightMaximum
            rightMaximum = newMaximum

        return arr