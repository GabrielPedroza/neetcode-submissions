from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:

        memo = {}

        @cache
        def dp(n):
            if n >= len(nums): return 0

            return max(
                nums[n] + dp(n + 2),
                dp(n + 1)
            )

        return dp(0)