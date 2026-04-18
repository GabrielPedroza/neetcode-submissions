class Solution:
    DELIMITER = "$"

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(string)}{self.DELIMITER}{string}" for string in strs)

    def decode(self, s: str) -> List[str]:
        output = []

        i = 0
        while i < len(s):
            j = s.find(self.DELIMITER, i)
            len_of_word = int(s[i:j])
            start = j + 1
            end = start + len_of_word
            output.append(s[start:end])

            i = end

        return output
