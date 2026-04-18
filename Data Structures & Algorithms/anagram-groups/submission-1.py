class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(list)

        for string in strs:
            bucket = [0] * 26

            for ch in string:
                bucket[ord(ch) - ord('a')] += 1

            output[str(bucket)].append(string)

        return output.values()
