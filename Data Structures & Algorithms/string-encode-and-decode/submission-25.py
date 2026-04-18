class Solution:

    def encode(self, strs: List[str]) -> str:
        output = []

        for string in strs:
            output.append(str(len(string)) + '!' + string)

        return ''.join(output)

    def decode(self, s: str) -> List[str]:
        output = []

        i = 0

        while i < len(s):
            length = []
            while s[i].isnumeric():
                length.append(s[i])
                i += 1
            
            i += 1

            lengthOfWord = int(''.join(length))
            startOfWord = i

            output.append(s[startOfWord:startOfWord + lengthOfWord])

            i += lengthOfWord
        
        return output