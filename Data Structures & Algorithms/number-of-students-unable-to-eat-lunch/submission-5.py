class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        res = len(students)
        student_count = Counter(students)

        for sandwich in sandwiches:
            if student_count[sandwich] > 0:
                res -= 1
                student_count[sandwich] -= 1
            else:
                return res

        return res