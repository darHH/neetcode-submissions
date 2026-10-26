from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        island_count = 0

        for row in range(rows):
            for col in range(cols):
                # new unvisited land cell means a new island 
                if grid[row][col] == "1":
                    island_count += 1
                    # mark visited as soon as cell is queued so its never queued twice
                    grid[row][col] = "0"
                    queue = deque([(row,col)])

                    # BFS flood fill - sink every connected land cell 
                    while queue:
                        r, c = queue.popleft()

                        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                                grid[nr][nc] = "0"
                                queue.append((nr,nc))

        return island_count