class Solution:

    def encode(self, strs: List[str]) -> str:
        delimiter_list = []

        for string in strs:
            delimiter_list.append(str(len(string)) + '!' + string)
        
        return ''.join(delimiter_list)

    def decode(self, s: str) -> List[str]:
        output = []

        curr_index = 0

        while curr_index < len(s):
            end_numeric = curr_index
            while s[end_numeric] != '!':
                end_numeric += 1
            length = int(s[curr_index:end_numeric])

            starting_ch = end_numeric + 1
            ending_ch = starting_ch + length
            

            get_word = s[starting_ch:ending_ch]

            curr_index = ending_ch

            output.append(get_word)

        return output

