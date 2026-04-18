class Solution:
    def isPalindrome(self, s: str) -> bool:
        filteredString = [ch.lower() for ch in s if ch.isalnum()]

        return True if filteredString == list(reversed(filteredString)) else False