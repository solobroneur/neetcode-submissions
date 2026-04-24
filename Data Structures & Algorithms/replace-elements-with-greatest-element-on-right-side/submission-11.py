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