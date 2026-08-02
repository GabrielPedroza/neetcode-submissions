class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        path = []

        candidates.sort()

        def backtrack(start: int, current_sum: int):
            if current_sum == target:
                output.append(path[:])
                return
            
            if current_sum > target:
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                path.append(candidates[i])
                backtrack(i + 1, current_sum + candidates[i])
                path.pop()

        backtrack(0, 0)
        return output
