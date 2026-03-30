class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        elif x == 1:
            return 1

        lower = 0
        upper = x
        midpoint = x // 2
        
        while True:
            if midpoint * midpoint == x:
                return midpoint
            elif (midpoint * midpoint < x) and ((midpoint+1) * (midpoint + 1) > x):
                return midpoint
            elif midpoint * midpoint < x:
                lower = midpoint + 1
            else:
                upper = midpoint - 1
            midpoint = (lower + upper) // 2