class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores, score = list(), 0

        for operation in operations:
            if operation == "+":
                score += scores[-1] + scores[-2]
                scores.append(scores[-1] + scores[-2])
            elif operation.lower() == "d":
                score += scores[-1] * 2
                scores.append(scores[-1] * 2)
            elif operation.lower() == "c":
                score -= scores.pop()
            else:
                score += int(operation)
                scores.append(int(operation))

        return score