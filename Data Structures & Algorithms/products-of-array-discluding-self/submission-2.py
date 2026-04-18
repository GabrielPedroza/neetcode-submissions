class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)
        prefix = 1

        for idx, num in enumerate(nums):
            output[idx] = prefix
            prefix *= num
        
        postfix = 1
        
        for idx, num in reversed(list(enumerate(nums))):
            output[idx] *= postfix
            postfix *= num
        
        return output