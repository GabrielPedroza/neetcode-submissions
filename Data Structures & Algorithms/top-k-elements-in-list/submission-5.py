class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        frequency = [[] for _ in range(len(nums) + 1)]

        for num, freq in counter.items():
            frequency[freq].append(num)
        
        output = []

        for i in range(len(frequency) - 1, - 1, - 1):
            for num in frequency[i]:
                output.append(num)
                if len(output) == k: return output
        
        return output
