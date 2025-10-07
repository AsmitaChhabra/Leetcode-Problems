

# Code
```python3 []
import heapq
from collections import defaultdict

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        next_rain = defaultdict(list)
        
        # Store all rain days for each lake
        for i, lake in enumerate(rains):
            if lake > 0:
                next_rain[lake].append(i)
        
        full = set()          # lakes currently full
        heap = []             # (next_rain_day, lake)
        ans = [-1] * n        # result array
        
        for i, lake in enumerate(rains):
            if lake > 0:  # rainy day
                next_rain[lake].pop(0)  # remove today's rain from list
                
                if lake in full:        # flood check
                    return []
                
                full.add(lake)
                
                # if lake will rain again, track its next rain day
                if next_rain[lake]:
                    heapq.heappush(heap, (next_rain[lake][0], lake))
            
            else:  # sunny day
                if heap:  # dry the lake that rains soonest
                    _, dry_lake = heapq.heappop(heap)
                    ans[i] = dry_lake
                    full.remove(dry_lake)
                else:
                    ans[i] = 1  # dry any lake (doesn't matter)
        
        return ans

```
