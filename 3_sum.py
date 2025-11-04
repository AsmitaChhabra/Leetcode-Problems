
# Code
```python3 []
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()  # Step 1: sort the array to simplify duplicate handling
        
        for i in range(len(nums) - 2):
            # Skip duplicate values for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left, right = i + 1, len(nums) - 1  # Two-pointer setup
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total < 0:
                    left += 1  # need a larger sum
                elif total > 0:
                    right -= 1  # need a smaller sum
                else:
                    # Found a triplet
                    res.append([nums[i], nums[left], nums[right]])
                    
                    # Move left and right to skip duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    # Move both pointers after processing
                    left += 1
                    right -= 1
                    
        return res

```
