class Solution:
    def isPalindrome(self, s: str) -> bool:
        filteredString = []

        for ch in s:
            if ch.isalnum():
                filteredString.append(ch.lower())
        
        l = 0
        r = len(filteredString) - 1

        while l < r:
            leftCh = filteredString[l]
            rightCh = filteredString[r]

            if leftCh != rightCh:
                return False
            
            l += 1
            r -= 1
        
        return True