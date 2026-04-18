class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dups = set()
        mf = 0

        l = 0

        for r in range(len(s)):
            while s[r] in dups:
                dups.remove(s[l])
                l += 1
            
            mf = max(mf, r - l + 1)
            dups.add(s[r])
        
        return mf