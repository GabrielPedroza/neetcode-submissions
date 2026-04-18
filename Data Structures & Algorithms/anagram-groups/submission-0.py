class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(list)

        for string in strs:
            sortedString = ''.join(sorted(string))

            output[sortedString].append(string)

        return output.values()
