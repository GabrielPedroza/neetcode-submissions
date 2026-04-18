class Solution:

    def encode(self, strs: List[str]) -> str:
        output = []

        for string in strs:
            output.append(str(len(string)) + "$" + string)
        
        return ''.join(output)

    def decode(self, s: str) -> List[str]:
        output = []

        i = 0

        while i < len(s):
            lenOfString = []
            start = i

            while s[start].isnumeric():
                lenOfString.append(s[start])
                start += 1
            
            start += 1
            lenOfString = int(''.join(lenOfString))

            output.append(s[start:start+lenOfString])

            i = start + lenOfString
        
        return output