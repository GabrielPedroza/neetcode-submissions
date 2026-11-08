class Solution:
    def longestPalindrome(self, s: str) -> str:
        output = s[0] if s else ""
        n = len(s)

        for i in range(1, n):
            for j, k in [(i, i), (i - 1, i)]:
                curr = self.currentPalindromeLength(j, k, s)
                if len(curr) > len(output):
                    output = curr
        
        return output
        
    def currentPalindromeLength(self, j: int, k: int, s: str) -> str:
        while j >= 0 and k < len(s) and s[j] == s[k]:
            j -= 1
            k += 1

        return s[j+1:k]