class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        longest_prefix = strs[0]

        for i in range(1, len(strs)):
            while longest_prefix not in strs[i]:
                longest_prefix = longest_prefix[:-1]
            if longest_prefix == "":
                return longest_prefix

        return longest_prefix