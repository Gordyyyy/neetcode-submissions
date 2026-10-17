class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxAreaSoFar = (len(heights)-1) * min(heights[0],heights[-1])
        p1 = 0
        p2 = len(heights) - 1
        
        while p2 > p1:
            if heights[p1] < heights[p2]:
                p1 += 1
            elif heights[p1] >= heights[p2]:
                p2 -= 1
            currentArea = (p2-p1) * min(heights[p1],heights[p2])
            if currentArea > maxAreaSoFar:
                maxAreaSoFar = currentArea
        return maxAreaSoFar
