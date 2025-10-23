

# Code
```python3 []
class Solution:
    def findDisappearedNumbers(self, nums):
        n = len(nums)
        full_set = set(range(1, n + 1))
        num_set = set(nums)
        return list(full_set - num_set)

```
