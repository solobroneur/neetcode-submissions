class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = list()

        for i, operation in enumerate(operations):
            print(i, operation)
            if operation == "+":
                first = int(score[len(score) - 1])
                second = int(score[len(score) - 2])
                score.append(first + second)
            elif operation.lower() == "d":
                last = int(score[len(score) - 1])
                score.append(last * 2)
            elif operation.lower() == "c":
                score.pop()
            else:
                score.append(int(operation))

        print(score)
        return sum(score)