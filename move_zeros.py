
# Code
```python3 []
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        pos = 0  # position to place the next non-zero element

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[pos] = nums[pos], nums[i]
                pos += 1

```
