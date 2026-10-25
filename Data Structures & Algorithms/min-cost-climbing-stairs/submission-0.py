from functools import cache
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        @cache
        def dfs(n, total):
            if n >= len(cost): return total
            if n == len(cost) - 1: return total + cost[n]
        
            return min(dfs(n + 1, total + cost[n]), dfs(n + 2, total + cost[n]))

        return min(dfs(0, 0), dfs(1, 0))