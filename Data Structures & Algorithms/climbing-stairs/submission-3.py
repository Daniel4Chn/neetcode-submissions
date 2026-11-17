class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [0 for i in range(n+1)]
        i = n-2
        if n == 1:
            return 1
        elif n == 2:
            return 2
        cache[-1] = 1
        cache[-2] = 1
        
        while i >= 0:
            cache[i] = cache[i+1] + cache[i+2]
            i-=1
        
        return cache[0]
