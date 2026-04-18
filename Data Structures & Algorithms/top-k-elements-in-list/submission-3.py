class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, freq in counter.items():
            buckets[freq].append(num)
        
        output = []

        for bucket in range(len(buckets) - 1, -1, -1):
            for num in buckets[bucket]:
                output.append(num)
                if len(output) == k:
                    return output