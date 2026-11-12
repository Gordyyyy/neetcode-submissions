from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # BFS
        # 1. setup
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        rows,cols = len(grid),len(grid[0])
        visited = set()
        toVisit = deque()
        countNumIslands = 0
        # 2. Find startPoint. whenever we find a point that's not visited, add 1
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1' and (row,col) not in visited:
                    currRow,currCol = row,col
                    toVisit.append((currRow,currCol))
                    visited.add((currRow,currCol))
                    countNumIslands += 1
                # We found a new island, find remaining around.
                    while toVisit:
                        currRow,currCol= toVisit.popleft()
                        for (drow,dcol) in directions:
                            newRow,newCol = currRow + drow, currCol + dcol
                            if (0 <= newRow < rows and 
                            0 <= newCol < cols and 
                            grid[newRow][newCol] == '1' and
                            (newRow,newCol) not in visited):
                                toVisit.append((newRow,newCol))
                                visited.add((newRow,newCol))
        return countNumIslands




            