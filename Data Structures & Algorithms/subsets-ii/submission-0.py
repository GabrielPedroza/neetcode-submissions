class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        output = []
        path = []

        nums.sort()

        def backtrack(start):
            output.append(path[:])

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue

                path.append(nums[i])
                backtrack(i + 1)
                path.pop()

        backtrack(0)
        return output
