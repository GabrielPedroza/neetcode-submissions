class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        path = []

        def backtrack(start, curr):
            if curr == target:
                output.append(path[:])
                return
            
            if curr > target:
                return
            
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i, curr + nums[i])
                path.pop()
        
        backtrack(0, 0)

        return output