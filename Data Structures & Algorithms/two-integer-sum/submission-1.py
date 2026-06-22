class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = defaultdict(int)

        for index, num in enumerate(nums):
            potential = target - num

            if potential in hashmap:
                return [hashmap[potential], index]
            
            hashmap[num] = index
        
        return -1