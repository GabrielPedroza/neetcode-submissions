class Solution:
    def isPalindrome(self, s: str) -> bool:
        filteredString = []

        for ch in s:
            if ch.isalnum():
                filteredString.append(ch.lower())
        
        print(filteredString)
        
        return True if filteredString == list(reversed(filteredString)) else False