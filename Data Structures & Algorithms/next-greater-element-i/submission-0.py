class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        hash_map_idx = {}
        result_array = [-1 for _ in nums1]

        for i in range(len(nums1)):
            hash_map_idx[nums1[i]] = i

        stack = []

        for i in range(len(nums2)):
            current = nums2[i]
            while stack and current > stack[-1]:
                top = stack.pop()
                result_array[hash_map_idx[top]] = nums2[i]
            if current in hash_map_idx:
                stack.append(current)

        return result_array
        