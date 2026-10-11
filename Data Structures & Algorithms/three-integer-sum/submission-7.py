class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3: return []
        output = []

        nums.sort()

        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]
                distinct = tuple((nums[i], nums[j], nums[k]))

                if total == 0 and distinct not in output:
                    output.append(tuple((nums[i], nums[j], nums[k])))
                    j += 1
                    k -= 1
                elif total < 0:
                    j += 1
                else:
                    k -= 1
        
        return output