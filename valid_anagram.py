

# Code
```python3 []
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Check if string t is an anagram of string s.
        An anagram has the same letters with the same counts, just in any order.
        """

        # Quick length check: if lengths differ, cannot be anagrams
        if len(s) != len(t):
            return False

        # Step 1: Count characters in s
        count_s = {}
        for char in s:
            # If char exists, increment count; else start at 1
            count_s[char] = count_s.get(char, 0) + 1

        # Step 2: Count characters in t
        count_t = {}
        for char in t:
            count_t[char] = count_t.get(char, 0) + 1

        # Step 3: Compare the two hashmaps
        # Python automatically returns True if counts match, False otherwise
        return count_s == count_t
