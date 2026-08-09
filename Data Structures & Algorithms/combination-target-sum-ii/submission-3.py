class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        path = []
        n = len(candidates)
        seen = set()

        candidates.sort()

        def backtrack(start, curr):
            if curr == target:
                output.append(path[:])
                return
            
            if curr > target:
                return
            
            for i in range(start, n):
                if i > start and candidates[i] == candidates[i - 1]: continue

                path.append(candidates[i])
                backtrack(i + 1, curr + candidates[i])
                path.pop()
        
        backtrack(0, 0)

        return output