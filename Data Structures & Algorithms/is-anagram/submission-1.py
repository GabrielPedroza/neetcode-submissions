class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagram_counter = Counter(s)

        for ch in t:
            if ch not in anagram_counter: return False
            if anagram_counter[ch] == 0: return False

            anagram_counter[ch] -= 1

            if anagram_counter[ch] == 0: del anagram_counter[ch]
        
        if len(anagram_counter): return False
        
        return True