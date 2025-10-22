

# Code
```python3 []
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n  # handle cases where k >= n

        # reverse entire array
        nums.reverse()

        # reverse first k elements
        nums[:k] = reversed(nums[:k])

        # reverse remaining n-k elements
        nums[k:] = reversed(nums[k:])

```
