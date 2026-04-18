class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftMax, rightMax = [0] * n, [0] * n

        leftMax[0] = height[0]
        for i in range(1, n):
            leftMax[i] = max(height[i], leftMax[i - 1])

        rightMax[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            rightMax[i] = max(height[i], rightMax[i + 1])
        
        res = 0
        for i in range(n):
            res += min(rightMax[i], leftMax[i]) - height[i]

        return res