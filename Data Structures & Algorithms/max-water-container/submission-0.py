class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWaterContainer = 0
        l = 0
        r = len(heights) - 1

        while l < r:
            currContainer = min(heights[l], heights[r]) * (r - l)
            maxWaterContainer = max(maxWaterContainer, currContainer)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return maxWaterContainer