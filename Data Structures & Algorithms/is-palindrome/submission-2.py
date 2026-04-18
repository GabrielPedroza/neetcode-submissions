class Solution:
    def isPalindrome(self, s: str) -> bool:
        filteredString = []

        for ch in s:
            if ch.isalnum():
                filteredString.append(ch.lower())
        
        print(filteredString)
        
        return True if ''.join(filteredString) == ''.join(list(reversed(filteredString))) else False