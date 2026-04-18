class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        heap = []

        for num, freq in counter.items():
            heap.append((freq, num))
        
        heapq.heapify_max(heap)

        return [heapq.heappop_max(heap)[1] for _ in range(k)]
