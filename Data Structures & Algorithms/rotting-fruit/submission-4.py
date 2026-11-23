from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # BFS
        rottened = set()
        toRotten = deque()
        rows,cols = len(grid),len(grid[0])

        directions = {(-1,0),(1,0),(0,-1),(0,1)}
        currTime = 0
        
        # Find the rotten fruits.
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    rottened.add((row,col))
                    toRotten.append((row,col,0))
        # Rottened fruit found. Rottened on day 0
        while toRotten:
            row,col,currTime = toRotten.popleft()
            for drow,dcol in directions:
                newRow,newCol = row + drow, col + dcol
                # valid check
                if (0 <= newRow < rows and 
                0 <= newCol < cols and
                grid[newRow][newCol] == 1 and 
                (newRow,newCol) not in rottened
                ):
                    rottened.add((newRow,newCol))
                    toRotten.append((newRow,newCol,currTime+1))
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and (row,col) not in rottened:
                    return -1
        return currTime
        
        



    
    