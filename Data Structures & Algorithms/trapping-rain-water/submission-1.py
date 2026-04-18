class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        leftMaxWall, rightMaxWall = height[l], height[r]
        trappedWater = 0

        while l < r:
            if leftMaxWall > rightMaxWall:
                r -= 1
                rightMaxWall = max(rightMaxWall, height[r])
                trappedWater += rightMaxWall - height[r]
            else:
                l += 1
                leftMaxWall = max(leftMaxWall, height[l])
                trappedWater += leftMaxWall - height[l]

        return trappedWater