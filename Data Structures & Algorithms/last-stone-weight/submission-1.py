import heapq
class Solution:
    
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []

        for stone in stones:
            heap.append(-stone)
        
        heapq.heapify(heap)

        while len(heap) > 1:
            stone1 = -heapq.heappop(heap)
            stone2 = -heapq.heappop(heap)
            
            if stone1 == stone2:
                # damage
                continue
            else:
                diff = abs(stone1 - stone2)
                heapq.heappush(heap,-diff)
        if len(heap) == 1:
            return -heap[0]
        else:
            return 0
