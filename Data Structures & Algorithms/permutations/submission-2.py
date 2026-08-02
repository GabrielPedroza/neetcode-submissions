class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        path = []
        seen = set()

        def backtrack():
            if len(path) == len(nums):
                output.append(path[:])
                return

            for i in range(len(nums)):
                if (current_num := nums[i]) not in seen:
                    seen.add(current_num)
                    path.append(current_num)

                    backtrack()

                    seen.remove(current_num)
                    path.pop()
        
        backtrack()
        return output