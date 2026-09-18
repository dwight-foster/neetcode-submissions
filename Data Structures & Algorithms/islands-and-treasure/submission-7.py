class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        seen = set()
        INF = 2147483647
        q = []

        def add_cell(r, c):
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == -1 or (r,c) in seen:
                return
            seen.add((r, c))
            q.append((r, c))

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    q.append((i,j))
                    seen.add((i,j))
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.pop(0)
                grid[r][c] = dist
                add_cell(r + 1, c)
                add_cell(r, c + 1)
                add_cell(r - 1, c)
                add_cell(r, c - 1)
            dist += 1
        
