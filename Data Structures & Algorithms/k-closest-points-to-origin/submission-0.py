import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        result = []

        for point in points:
            (x,y) = point
            distance = (x**2 + y**2)
            t = (distance,x,y)
            heap.append(t)
        # Now I have my heap filled with point and their distance from low to high
        
        heapq.heapify(heap)
        for time in range(k):
            distance,x,y = heapq.heappop(heap)
            result.append([x,y])
        return result



        

        