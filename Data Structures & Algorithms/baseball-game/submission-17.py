class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = list()

        for i, operation in enumerate(operations):
            if operation == "+":
                score.append(score[-1] + score[-2])
            elif operation.lower() == "d":
                score.append(score[-1] * 2)
            elif operation.lower() == "c":
                score.pop()
            else:
                score.append(int(operation))

        return sum(score)