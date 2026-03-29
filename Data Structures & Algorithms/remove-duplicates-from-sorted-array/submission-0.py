class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 1

        k = 0

        while i < len(nums):
            if i == len(nums) - 1:
                return k + 1
            elif nums[i] == nums[j]:
                nums.pop(j)
            else:
                i += 1
                j += 1
                k += 1

        return k