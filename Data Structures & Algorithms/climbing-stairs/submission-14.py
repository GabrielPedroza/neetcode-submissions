class Solution:
    def dp(self, n):
        prev2, prev1 = 1, 1      

        for _ in range(2, n + 1):
            current = prev2 + prev1

            prev2 = prev1
            prev1 = current

        return prev1

    def climbStairs(self, n: int) -> int:
        return self.dp(n)