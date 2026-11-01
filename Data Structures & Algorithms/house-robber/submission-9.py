from functools import cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 0: return 0
        if n == 1: return nums[0]

        rob2 = nums[0]
        rob1 = max(nums[0], nums[1])

        for i in range(2, n):
            current = max(rob2 + nums[i], rob1)

            rob2 = rob1
            rob1 = current
        
        return rob1