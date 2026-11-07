
class Solution:
    
    def dp(self, n):
        if n in self.cache:
            return self.cache[n]

        if n < 0:
            return 0
        
        if n == 0:
            return 1
        
        self.cache[n] = self.dp(n-1) + self.dp(n-2)
        return self.cache[n]

    def climbStairs(self, n: int) -> int:
        self.cache = {}
        return self.dp(n)