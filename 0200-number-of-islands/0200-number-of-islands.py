class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[-1]*n for _ in range(m)]

        def visit(i: int, j: int):
            visited[i][j] = 1
            directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]

            for dx,dy in directions:
                x, y = dx + i, dy + j
                if 0 <= x < m and 0 <= y < n and grid[x][y] == '1' and visited[x][y] == -1:
                    visit(x, y)

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and visited[i][j] == -1:
                    visit(i, j)
                    count += 1

        return count