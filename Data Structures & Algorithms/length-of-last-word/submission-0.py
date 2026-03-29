class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        i = len(s) - 1

        length = 0

        while s[i] == " ":
            i -= 1

        while i >= 0:
            if s[i] == " ":
                return length
            else:
                length += 1
                i -= 1
            
        return length