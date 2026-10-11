class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for string in strs:
            bucket = [0] * 26
            for ch in string:
                bucket[ord(ch) - ord('a')] += 1
            
            hashmap[tuple(bucket)].append(string)

        return list(hashmap.values())