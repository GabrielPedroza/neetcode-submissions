class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longestSequence = 0
        store = set(nums)

        for num in nums:
            if num - 1 in store:
                continue
            
            currSequence = 1
            currNum = num
            while currNum + 1 in store:
                currNum += 1
                currSequence += 1
            
            longestSequence = max(longestSequence, currSequence)
        
        return longestSequence