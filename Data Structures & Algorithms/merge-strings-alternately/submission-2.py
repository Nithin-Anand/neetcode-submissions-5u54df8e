class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        combined = []

        for i in range(max(len(word1), len(word2))):
            if i >= len(word1):
                return ''.join(combined + list(word2[i:]))
            elif i >= len(word2):
                return ''.join(combined + list(word1[i:]))
            else:
                combined.append(word1[i])
                combined.append(word2[i])


        return ''.join(combined)
        
            
        
            