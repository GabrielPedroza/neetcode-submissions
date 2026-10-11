class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        total = 0
        nums = set(nums)

        for num in nums:
            if num - 1 in nums: continue

            current_num = num
            count = 1
            while current_num + 1 in nums:
                count += 1
                current_num += 1

            total = max(total, count)   

        return total