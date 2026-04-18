class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        postfix = [0] * len(nums)

        prefix_multiplier = 1
        
        for idx, num in enumerate(nums):
            prefix_multiplier *= num
            prefix[idx] = prefix_multiplier
        
        postfix_multiplier = 1

        for idx, num in reversed(list(enumerate(nums))):
            postfix_multiplier *= num
            postfix[idx] = postfix_multiplier
        
        output = [0] * len(nums)

        for i in range(len(nums)):
            if i == 0:
                output[i] = postfix[i + 1]
                continue
            
            if i == len(nums) - 1:
                output[i] = prefix[i - 1]
                continue
            
            prefixNum = prefix[i - 1]
            postfixNum = postfix[i + 1]

            output[i] = prefixNum * postfixNum
        
        return output



