class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hash_map = {}

        for k, v in enumerate(nums):
            hash_map[v] = k

        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in hash_map and hash_map[difference] != i:
                return [i, hash_map[difference]]