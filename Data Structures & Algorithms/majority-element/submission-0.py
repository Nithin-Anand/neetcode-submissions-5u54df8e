class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        nums_hashmap = {}

        for num in nums:
            count = nums_hashmap.get(num, 0) + 1

            if count > len(nums) / 2:
                return num
            
            nums_hashmap[num] = count

        

        