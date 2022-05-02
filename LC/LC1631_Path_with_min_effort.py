from typing import List
import math
import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row = len(heights)
        col = len(heights[0])
        self.maxSoFar = math.inf
        dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        def dfs(x, y, maxDifference):
            if (x == row - 1 or y == col - 1):
                self.maxSoFar = min(self.maxSoFar, maxDifference)
                return maxDifference
            currentHeight = heights[x][y]
            heights[x][y] = 0
            minEffort = math.inf
            for dx, dy in dir:
                adjacentX = x + dx
                adjacentY = y + dy
                if 0 <= adjacentX < row and 0 <= adjacentY < col and heights[adjacentX][adjacentY] != 0:
                    currentDifference = abs(heights[adjacentX][adjacentY] - currentHeight)
                    maxCurrentDifference = max(currentDifference, maxDifference)
                    if maxCurrentDifference < self.maxSoFar:
                        result = dfs(adjacentX, adjacentY, maxCurrentDifference)
                        minEffort = min(minEffort, result)
            heights[x][y] = currentHeight
            return minEffort
        
        return dfs(0, 0, 0)
    def minimumEffortPath2(self, heights):
        row = len(heights)
        col = len(heights[0])
        differenceMatrix = [[math.inf] * col for _ in range(row)]
        differenceMatrix[0][0] = 0
        visited = [[False] * col for _ in range(row)]
        queue = [(0,0,0)]
        while queue:
            difference, x, y = heapq.heappop(queue)
            visited[x][y] = True
            for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                adjacentX = x + dx
                adjacentY = y + dy
                if (0 <= adjacentX < row and 0 <= adjacentY < col and not visited[adjacentX][adjacentY]):
                    currentDifference = abs(heights[adjacentX][adjacentY] - heights[x][y])
                    maxDifference = max(currentDifference, differenceMatrix[x][y])
                    if differenceMatrix[adjacentX][adjacentY] > maxDifference:
                        differenceMatrix[adjacentX][adjacentY] = maxDifference
                        heapq.heappush(queue, (maxDifference, adjacentX, adjacentY))
        return differenceMatrix[-1][-1]
                        
                    
            
        
def main():
    heights = [[1,2,2],[3,8,2],[5,3,5]]
    s = Solution()
    print (s.minimumEffortPath2(heights))
    
main()