from functools import cache

class Solution:
    def climbStairs(self, n: int) -> int:
        memo = defaultdict(int)

        @cache
        def dp(step):
            if step <= 2: return step

            # if step in memo:
            #     return memo[step]
            
            # memo[step] = dp(step - 1) + dp(step - 2)

            # return memo[step]
            return dp(step - 1) + dp(step - 2)
        
        return dp(n)