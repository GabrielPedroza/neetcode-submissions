class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums[0], nums[1])
        
        return max(nums[0], self.rob_helper(nums[1:]), self.rob_helper(nums[:-1]))
    
    def rob_helper(self, nums: List[int]) -> int:
        n = len(nums)

        rob2 = nums[0]
        rob1 = max(nums[0], nums[1])
        
        for i in range(2, n):
            current = max(rob2 + nums[i], rob1)

            rob2 = rob1
            rob1 = current
        
        return rob1