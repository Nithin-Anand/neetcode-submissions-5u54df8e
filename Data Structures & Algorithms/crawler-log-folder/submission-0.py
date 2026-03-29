class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = 0

        for log in logs:
            if log == "../":
                if stack == 0:
                    continue
                else:
                    stack -= 1
            elif log == "./":
                continue
            else:
                stack += 1
        
        return stack