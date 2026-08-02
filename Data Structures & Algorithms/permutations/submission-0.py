class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        path = []

        def backtrack():
            if len(path) == len(nums):
                output.append(path[:])
                return

            for i in range(len(nums)):
                if nums[i] not in path:
                    path.append(nums[i])
                    backtrack()
                    path.pop()
        
        backtrack()
        return output