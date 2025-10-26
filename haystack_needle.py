

# Code
```python3 []
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # if needle is empty, return 0
        if not needle:
            return 0
        
        # loop through haystack and check each substring
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1

```
