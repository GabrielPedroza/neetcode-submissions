class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0) # sentinel - flush the stack completely
        stack = []
        largest = 0

        for i, height in enumerate(heights):
            start = i

            while stack and stack[-1][1] > height:
                stackI, stackH = stack.pop()
                largest = max(largest, stackH * (i - stackI))

                start = stackI

            stack.append((start, height))

        return largest

    # [7,1,7,2,2,4]
    #                         