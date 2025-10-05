Testing a valid palindrome


# Code
```python3 []
class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = ''.join(ch.lower() for ch in s if ch.isalnum())

        return filtered == filtered[::-1]        
```
