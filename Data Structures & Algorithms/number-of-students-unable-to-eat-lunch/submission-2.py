class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        num_of_rejects = 0;

        while sandwiches and len(students) > num_of_rejects:
            student = students.pop(0)

            if sandwiches[0] == student:
                num_of_rejects = 0
                del sandwiches[0]
            else:
                num_of_rejects += 1
                students.append(student)

        return len(students)

        