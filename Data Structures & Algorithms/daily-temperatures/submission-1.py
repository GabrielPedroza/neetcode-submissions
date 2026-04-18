class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0] * len(temperatures)

        for idx, temp in enumerate(temperatures):
            if not stack or stack[-1][0] > temp:
                stack.append((temp, idx))
            else:
                while stack and stack[-1][0] < temp:
                    stackTemp, stackIdx = stack.pop()
                    output[stackIdx] = idx - stackIdx
                
                stack.append((temp, idx))
        
        return output