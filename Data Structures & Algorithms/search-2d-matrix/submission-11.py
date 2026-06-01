class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix) - 1

        while top <= bottom:
            middle_row = (top + bottom) // 2

            if target < matrix[middle_row][0]:
                bottom = middle_row - 1
            elif target > matrix[middle_row][-1]:
                top = middle_row + 1
            else:
                break

        if top > bottom:
            return False

        row = matrix[(top + bottom) // 2]
        left, right = 0, len(row) - 1

        while left <= right:
            middle = (left + right) // 2

            if target < row[middle]:
                right = middle - 1
            elif target > row[middle]:
                left = middle + 1
            else:
                return True
        
        return False

