class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique = []
        for i in nums:
            if i not in unique:
                unique.append(i)
            else:
                return True

        return False
        