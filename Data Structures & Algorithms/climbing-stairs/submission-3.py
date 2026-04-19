class Solution:
    def climbStairs(self, n: int) -> int:
        return self.climbStairs_cached(n, cache={})

    def climbStairs_cached(self, n: int, cache: dict) -> int:
        if n == 0:
            return 1
        elif n < 0:
            return 0
        elif n in cache:
            return cache[n]
        else:
            total = sum([self.climbStairs_cached(n-1, cache), self.climbStairs_cached(n-2, cache)])
            cache[n] = total

            return total


