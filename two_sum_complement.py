

# Code
```python3 []
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        Return indices of the two numbers in nums that add up to target.
        """
        
        # Step 1: Create an empty hashmap to store number -> index
        num_to_index = {}
        
        # Step 2: Iterate through the list
        for i, num in enumerate(nums):
            # Step 3: Compute the complement
            complement = target - num
            
            # Step 4: Check if complement is already in the hashmap
            if complement in num_to_index:
                # Found the pair, return their indices
                return [num_to_index[complement], i]
            
            # Step 5: Store the current number and its index in the hashmap
            num_to_index[num] = i
        
        # Step 6: If no solution found (problem guarantees there is one)
        return []

```
