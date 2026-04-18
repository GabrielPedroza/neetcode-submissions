class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counterForS = Counter(s)
        counterForT = Counter(t)

        return counterForS == counterForT