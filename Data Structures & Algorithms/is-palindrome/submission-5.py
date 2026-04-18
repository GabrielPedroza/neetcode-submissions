class Solution:
    def isPalindrome(self, s: str) -> bool:
        filteredString = [ch.lower() for ch in s if ch.isalnum()]

        return True if filteredString == filteredString[::-1] else False