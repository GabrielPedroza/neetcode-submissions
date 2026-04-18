class Solution:
    DELIMITER = "$"

    def encode(self, strs: List[str]) -> str:
        output = []

        for string in strs:
            output.append(str(len(string)) + self.DELIMITER + string)

        return ''.join(output)

    def decode(self, s: str) -> List[str]:
        output = []

        i = 0
        while i < len(s):
            lenOfStringArray = []
            while s[i] != self.DELIMITER:
                lenOfStringArray.append(s[i])
                i += 1
            
            start = i + 1
            lenOfString = start + int(''.join(lenOfStringArray))

            output.append(s[start:lenOfString])
            i = lenOfString

        return output
