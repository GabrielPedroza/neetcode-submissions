class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2

            curr_num = nums[mid]

            if curr_num == target:
                return mid
            elif curr_num > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return -1