class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        bijection_map = {}
        bijection_map_flipped = {}

        split_strings = s.split(" ")

        if len(pattern) != len(split_strings):
            return False


        for i in range(len(split_strings)):
            key = list(pattern)[i]
            value = split_strings[i]
            print(key, value)

            if key not in bijection_map and value not in bijection_map_flipped:
                bijection_map[key] = value
                bijection_map_flipped[value] = key
                continue
            elif key in bijection_map and value not in bijection_map_flipped:
                return False
            elif key not in bijection_map and value in bijection_map_flipped:
                return False
            elif bijection_map[key] != value:
                return False
            elif bijection_map_flipped[value] != key:
                return False
            
        
        return True