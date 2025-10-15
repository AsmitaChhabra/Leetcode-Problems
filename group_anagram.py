
# Code
```python3 []
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        anagrams = defaultdict(list)
        
        for word in strs:
            # Sort letters in word → becomes the hash key
            key = ''.join(sorted(word))
            anagrams[key].append(word)
        
        return list(anagrams.values())

```
