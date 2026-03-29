class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        index1 = 0
        index2 = 1

        for i in range(index1, len(numbers)):
            difference = target - numbers[index1]
            for j in range(index2, len(numbers)):
                if numbers[j] == difference:
                    return [index1 + 1, j + 1]
                    
            index1 += 1
            index2 += 1
                

