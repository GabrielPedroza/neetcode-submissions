class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        storage = defaultdict(list)

        for word in strs:
            sorted_word = ''.join(sorted(word))

            storage[sorted_word].append(word)
        
        return list(storage.values())