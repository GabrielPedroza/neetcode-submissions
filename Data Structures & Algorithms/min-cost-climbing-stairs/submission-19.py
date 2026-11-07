
from functools import cache
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        N = len(cost)
        prev2, prev1 = cost[0], cost[1]
        
        for i in range(2, N):
            current = cost[i] + min(prev2 , prev1)

            prev2 = prev1
            prev1 = current

        return min(prev2, prev1)