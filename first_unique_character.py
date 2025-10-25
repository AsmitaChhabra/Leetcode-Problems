
# Code
```python3 []
class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter
        
        # Count frequency of each character
        count = Counter(s)
        
        # Loop again to find the first character with frequency 1
        for i, ch in enumerate(s):
            if count[ch] == 1:
                return i
        
        # If no unique character found
        return -1

```
