class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 2: return 0

        l, r = 0, len(height) - 1
        trappedWater = 0

        maxLeftBar, maxRightBar = height[l], height[r]

        while l < r:
            if maxLeftBar > maxRightBar:
                r -= 1
                maxRightBar = max(maxRightBar, height[r])
                trappedWater += maxRightBar - height[r]
            else:
                l += 1
                maxLeftBar = max(maxLeftBar, height[l])
                trappedWater += maxLeftBar - height[l]

        return trappedWater