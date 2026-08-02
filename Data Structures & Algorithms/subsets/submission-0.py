class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        path = []

        def backtrack(start):
            output.append(path[:])

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1)
                path.pop()
        
        backtrack(0)
        return output