class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_maps = []
        group_strings = []
        unique_maps = []
        for string in strs:
            hash_map = {}
            for char in list(string):
                hash_map[char] = hash_map.get(char, 0) + 1

            hash_maps.append([string, hash_map])


            
        for i in range(len(hash_maps)):
            new = True
            for j in range(len(unique_maps)):
                if hash_maps[i][1].items() == unique_maps[j].items():
                    group_strings[j].append(hash_maps[i][0])
                    new = False
                    break
            if new:
                unique_maps.append(hash_maps[i][1])
                group_strings.append([hash_maps[i][0]])


        return group_strings