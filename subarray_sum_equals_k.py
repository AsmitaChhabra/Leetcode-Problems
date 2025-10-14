
# Code
```python3 []
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_count = {0: 1}   # base case: prefix sum 0 occurs once
        current_sum = 0
        count = 0

        for num in nums:
            current_sum += num

            # if (current_sum - k) was seen before, we found that many subarrays
            if current_sum - k in prefix_count:
                count += prefix_count[current_sum - k]

            # record the current prefix sum in the map
            prefix_count[current_sum] = prefix_count.get(current_sum, 0) + 1

        return count

```
