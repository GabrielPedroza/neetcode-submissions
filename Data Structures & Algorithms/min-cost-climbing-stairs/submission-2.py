# from functools import cache

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        n = len(cost)

        prev2 = cost[0]
        prev1 = cost[1]

        for i in range(2, n):
            current = cost[i] + min(prev2, prev1)

            prev2 = prev1
            prev1 = current
        
        return min(prev2, prev1)

        # n = len(cost)

        # dp = [0] * (n + 1)

        # dp[0] = cost[0]
        # dp[1] = cost[1]

        # for i in range(2, n):
        #     dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
        
        # return min(dp[n - 1], dp[n - 2])

        # @cache
        # def dp(n):
        #     if n >= len(cost): return 0

        #     return cost[n] + min(dp(n + 1), dp(n + 2))
        
        # return min(dp(0), dp(1))