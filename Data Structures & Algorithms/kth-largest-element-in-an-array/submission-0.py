import heapq
class Solution:

    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:
            heap.append(-num)
        
        heapq.heapify(heap)
        # Now I have my heap list heapified

        for time in range(k):
            result = -1 * heapq.heappop(heap)
        
        return result

        