class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targets = {}
        
        for idx, num in enumerate(nums):
            targetNum = target - num

            if targetNum in targets:
                return [targets[targetNum], idx]

            targets[num] = idx
        
        return []