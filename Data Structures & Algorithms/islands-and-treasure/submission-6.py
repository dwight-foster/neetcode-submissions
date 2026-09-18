class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        seen = set()
        INF = 2147483647
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        def dfs(r, c):
            if (r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == -1):
                return INF
            if (r, c) in seen:
                return grid[r][c]
            if grid[r][c] == 0:
                return 0

            seen.add((r, c))
            path = INF

            for dr, dc in directions:
                out = dfs(r + dr, dc + c)+1
                path = min(path, out)
            grid[r][c] = min(grid[r][c], path)
            return path
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                seen = set()
                if grid[i][j] != 0 or grid[i][j] != -1:
                    dfs(i, j)
