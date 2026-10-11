class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        output = 0
        l, r = 1, max(piles)

        while l <= r:
            mid = l + (r - l) // 2
            speed = self.speedToEat(piles, mid)

            if speed <= h:
                output = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return output
    
    def speedToEat(self, piles: List[int], k: int) -> int:
        return sum([math.ceil(pile / k) for pile in piles])