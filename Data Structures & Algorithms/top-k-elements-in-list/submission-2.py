class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)

        for num in nums:
            counter[num] += 1

        heap = [(-freq, num) for num, freq in counter.items()]

        heapq.heapify(heap)

        return [heapq.heappop(heap)[1] for _ in range(k)]