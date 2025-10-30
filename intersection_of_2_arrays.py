

# Code
```python3 []
from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Step 1️⃣: Count frequency of each number in both arrays
        count1 = Counter(nums1)   # Example: nums1 = [1,2,2,1] → {1: 2, 2: 2}
        count2 = Counter(nums2)   # Example: nums2 = [2,2]   → {2: 2}

        result = []  # To store the intersection elements

        # Step 2️⃣: Loop through each unique element in nums1
        for num in count1:
            # Step 3️⃣: Check if that number also exists in nums2
            if num in count2:
                # Step 4️⃣: Find how many times it appears in BOTH arrays
                # (The smaller count between the two)
                common_count = min(count1[num], count2[num])

                # Step 5️⃣: Add that number to the result 'common_count' times
                # Example: if num=2 and common_count=2 → add [2,2]
                result.extend([num] * common_count)

        # Step 6️⃣: Return the intersection list
        return result

```
