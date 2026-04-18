class Solution:
    DELIMITER = "$"

    def encode(self, strs: List[str]) -> str:
        return ''.join(f"{len(string)}{self.DELIMITER}{string}" for string in strs)

    def decode(self, s: str) -> List[str]:
        output = []

        i = 0
        while i < len(s):
            j = s.find(self.DELIMITER, i)
            lenOfString = s[i:j]
            start = j + 1
            end = start + int(lenOfString)

            output.append(s[start:end])

            i = end
        
        return output