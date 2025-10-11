
# Code
```python3 []
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        pos = 0  # next spot for a non-zero
        for num in nums:
            if num != 0:
                nums[pos] = num
                pos += 1

        # Fill the remaining positions with zeros
        while pos < len(nums):
            nums[pos] = 0
            pos += 1

        
```
