class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        path = []

        def backtrack(start, current_sum):
            if current_sum == target:
                output.append(path[:])
                return

            if current_sum > target:
                return

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i, current_sum + nums[i])
                path.pop()

        backtrack(0, 0)
        return output
