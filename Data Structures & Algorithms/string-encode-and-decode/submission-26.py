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
            start = i
            curr_str_len = []

            while s[start] != "$":
                curr_str_len.append(s[start])
                start += 1
            
            start += 1
            curr_str_len = int(''.join(curr_str_len))
            end = start + curr_str_len
            output.append(s[start:end])

            i = end

        return output
