class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        storage = defaultdict(list)

        for word in strs:
            bucket = [0] * 26
            for ch in word:
                bucket[ord(ch) - ord('a')] += 1

            storage[tuple(bucket)].append(word)

        return list(storage.values())