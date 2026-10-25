# from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:

        memo = {}

        # @cache
        def dp(n):
            if n >= len(nums): return 0
            if n in memo:
                return memo[n]

            memo[n] = max(
                nums[n] + dp(n + 2),
                dp(n + 1)
            )

            return memo[n]

        return max(dp(0), dp(1))