##### 解题思路： 滑动窗口思想

```python
# 作者：力扣官方题解
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        ans = inf 
        cnt = 0 
        for i, ch in enumerate(blocks): 
            if ch == 'W':
                cnt += 1
            if i >= k and blocks[i-k] == 'W':
                cnt -= 1
            if i >= k - 1:
                ans = min(ans, cnt)
        return ans 


```
