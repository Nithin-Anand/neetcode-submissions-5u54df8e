class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1

        while i < j:
            print(i, j)
            midpoint = (i + j) // 2
            if nums[midpoint] == target:
                return midpoint
            elif nums[midpoint] < target:
                i = midpoint + 1
            else:
                j = midpoint - 1
        
        if nums[i] == target:
            return i
        else:
            return -1