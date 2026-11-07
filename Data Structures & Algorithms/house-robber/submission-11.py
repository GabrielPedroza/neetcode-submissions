
from functools import cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def dp(i):
            if i >= len(nums):
                return 0

            # we can rob current house and then + 2 from there

            # we can choose not to rob the house and rob + 1
            return max(nums[i] + dp(i+2), dp(i + 1))

        return dp(0)