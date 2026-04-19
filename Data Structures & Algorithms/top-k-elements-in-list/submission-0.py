class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}

        for num in nums:
            frequencies[num] = frequencies.get(num, 0) + 1
        
        heap = []
        for num in frequencies.keys():
            heapq.heappush(heap, (frequencies[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
            
        result = []
        for pair in heap:
            result.append(pair[1])

        return result