class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)

        a = None
        b = None
        
        count_map = dict.fromkeys([i for i in range(1, (n ** 2) + 1)], None)

        for i in range(0, n):
            for j in range(0, n):
                
                try:
                    count_map.pop(grid[i][j])
                except KeyError:
                    a = grid[i][j]
        
        b = list(count_map.keys())[0]

        return [a,b]






        