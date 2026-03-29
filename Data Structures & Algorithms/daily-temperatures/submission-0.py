class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        index_stack = []
        temperature_stack = []

        result = [0] * len(temperatures)

        for i in range(len(temperatures)):

            while temperature_stack and temperatures[i] > temperature_stack[-1]:
                index = index_stack.pop() 
                result[index] = i - index
                temperature_stack.pop()
            
            index_stack.append(i)
            temperature_stack.append(temperatures[i])
        
        return result
