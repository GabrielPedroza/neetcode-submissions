class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not len(nums):
            return 0
        
        longestConsecutiveSequence = 1
        sequenceSet = set(nums)

        for num in nums:
            if num - 1 in sequenceSet:
                continue
            
            currSequence = 0
            currNum = num
            
            while currNum in sequenceSet:
                currSequence += 1
                currNum += 1

            longestConsecutiveSequence = max(longestConsecutiveSequence, currSequence)    

        return longestConsecutiveSequence