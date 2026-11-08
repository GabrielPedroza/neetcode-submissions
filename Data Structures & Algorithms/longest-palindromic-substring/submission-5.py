class Solution:
    def longestPalindrome(self, s: str) -> str:
        output = s[0] if s else ""
        n = len(s)

        for i in range(1, n):
            currOdd = self.currentPalindromeLength(i, i, s)
            currEven = self.currentPalindromeLength(i, i-1, s)
            if len(currOdd) > len(output):
                output = currOdd
            if len(currEven) > len(output):
                output = currEven
        
        return output
        
    def currentPalindromeLength(self, j: int, k: int, s: str) -> str:
        while j >= 0 and k < len(s) and s[j] == s[k]:
            j -= 1
            k += 1
        
        return s[j+1:k]