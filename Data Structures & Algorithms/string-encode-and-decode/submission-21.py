class Solution:

    def encode(self, strs: List[str]) -> str:
        output = []

        for string in strs:
            output.append(str(len(string)) + '!' + string)
        
        return ''.join(output)

    def decode(self, s: str) -> List[str]:
        output = []

        curr_index = 0

        while curr_index < len(s):
            delimiter = curr_index

            while s[delimiter] != '!':
                delimiter += 1
            
            length_of_word = int(s[curr_index:delimiter])

            start_ch = delimiter + 1
            ending_ch = start_ch + length_of_word

            output.append(s[start_ch:ending_ch])

            curr_index = ending_ch

        return output