from functools import cache
class Solution:
    
    @cache
    def dp(self, n):
        if n < 0:
            return 0
        
        if n == 0:
            return 1
        
        return self.dp(n-1) + self.dp(n-2)

    def climbStairs(self, n: int) -> int:
        self.cache = {}
        return self.dp(n)