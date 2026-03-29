class Solution:
    def scoreOfString(self, s: str) -> int:
        i = 0
        j = 1

        score = 0
        while j < len(s):
            score += abs(ord(s[i]) - ord(s[j]))

            i +=1
            j += 1
        return score