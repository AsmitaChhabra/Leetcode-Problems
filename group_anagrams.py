Explanation

This solution groups words that are anagrams by creating a unique “signature” for each word:
For each word, we sort its letters alphabetically and join them into a string using ''.join(sorted(word)).
Example: "eat", "tea", "ate" → "aet"
This ensures all anagrams share the same key.
We use a defaultdict(list) to automatically create a list for each new key.
Each word is appended to the list corresponding to its key.
At the end, we return all the lists of words from the dictionary, giving groups of anagrams.
Key idea: Sorting each word provides a consistent identifier for anagrams, allowing them to be grouped together efficiently.

# Code
```python3 []
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # Dictionary to hold groups of anagrams
        groups = defaultdict(list)

        for word in strs:
            # Create a sorted signature of the word
            key = ''.join(sorted(word))
            # Append word to the corresponding group
            groups[key].append(word)

        # Return all groups as a list
        return list(groups.values())

```
