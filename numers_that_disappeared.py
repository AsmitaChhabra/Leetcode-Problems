

# Code
```python3 []
from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            index = abs(num) - 1
            nums[index] = -abs(nums[index])  # mark as seen
        
        # collect all indices where value is still positive
        return [i + 1 for i, num in enumerate(nums) if num > 0]

```
