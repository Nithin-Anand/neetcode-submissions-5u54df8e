class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        new_arr = [0 for i in range(0, 2 * len(nums))]

        for i in range(len(nums)):
            new_arr[i] = nums[i]
            new_arr[i + len(nums)] = nums[i]

        return new_arr

