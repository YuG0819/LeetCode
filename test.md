```python
class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        f = [[0] * n for _ in range(2)]

        for i in range(m):
            pos = i % 2
            for j in range(n):
                if i > 0:
                    f[pos][j] = max(f[pos][j], f[1 - pos][j])
                if j > 0:
                    f[pos][j] = max(f[pos][j], f[pos][j - 1])
                f[pos][j] += grid[i][j]
        
        return f[(m - 1) % 2][n - 1]

```