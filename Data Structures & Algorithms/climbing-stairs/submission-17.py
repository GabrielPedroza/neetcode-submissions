class Solution:
    def dp(self, n):
        if n < 2: return 1
        dp = [0] * n
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n - 1] + dp[n - 2]

        return prev1

    def climbStairs(self, n: int) -> int:
        return self.dp(n)