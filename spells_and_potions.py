# Summary

Sort the potions array to enable binary search.

For each spell:

Calculate the minimum potion needed:
target = success/spell
 
Use binary search (bisect_left) to find the first potion ≥ target.

Count all potions from that index to the end → number of successful pairs.

Append the count to the result array.

Return the final result array.

Key points:
target is not an actual potion, it’s the threshold.
Sorting + binary search reduces complexity:

Example:
spells = [5,1,3]
potions = [1,2,3,4,5]
success = 7
Output: [4, 0, 3]
5 pairs with [2,3,4,5] → 4
1 pairs with none → 0
3 pairs with [3,4,5] → 3

# Code
```python3 []

from typing import List
from bisect import bisect_left

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        n = len(potions)
        result = []

        for spell in spells:
            target = success / spell
            idx = bisect_left(potions, target)  # Find first potion >= target
            count = n - idx  # Count of successful pairs
            result.append(count)

        return result  # <-- return OUTSIDE the for-loop

```
