class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        combined = []

        for i in range(max(len(word1), len(word2))):
            if i >= len(word1):
                combined.append(word2[i:])
                break
            elif i >= len(word2):
                combined.append(word1[i:])
                break
            else:
                combined.append(word1[i])
                combined.append(word2[i])


        return ''.join(combined)
        
            
        
            