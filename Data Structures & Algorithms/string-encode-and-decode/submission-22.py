class Solution:

    def encode(self, strs: List[str]) -> str:
        output = []
        
        for string in strs:
            output.append(str(len(string)) + '!' + string)

        return ''.join(output)

    def decode(self, s: str) -> List[str]:
        i = 0
        output = []
        while i < len(s):
            length = []
            while s[i].isnumeric():
                length.append(s[i])
                i += 1
            
            i += 1
            startOfWord = i
            
            lengthOfStr = int(''.join(length)) + startOfWord

            word = s[startOfWord:lengthOfStr]
            output.append(word)

            i = lengthOfStr

            # 4!neet4!code
            #      ^

        return output