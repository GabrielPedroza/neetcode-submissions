class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = self.parseString(s)

        return string == string[::-1]
    
    def parseString(self, s: str) -> str:
        output = []

        for ch in s:
            if not ch.isalnum(): continue
            output.append(ch.lower())

        return ''.join(output)