class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1_copy = nums1[:m]
        current_insertion_point = 0
        left, right = 0, 0
        length_of_sorted_array = m + n

        while current_insertion_point < length_of_sorted_array:
            right_has_no_nums_left = right >= n
            left_has_nums_left = left < m
            left_should_be_inserted = (
                left_has_nums_left
                and not right_has_no_nums_left
                and nums1_copy[left] <= nums2[right]
            )

            if right_has_no_nums_left or left_should_be_inserted:
                nums1[current_insertion_point] = nums1_copy[left]
                left += 1
            else:
                nums1[current_insertion_point] = nums2[right]
                right += 1

            current_insertion_point += 1
