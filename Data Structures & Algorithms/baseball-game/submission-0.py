class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        results = []

        for i in range(len(operations)):
            if operations[i] == '+':
                results.append(results[-2] + results[-1])
            elif operations[i] == 'C':
                results.pop()
            elif operations[i] == 'D':
                results.append(results[-1] * 2)
            else:
                results.append(int(operations[i]))
        
        return sum(results)
