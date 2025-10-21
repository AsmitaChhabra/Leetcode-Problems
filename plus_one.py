

# Code
```python3 []
class Solution:
    def plusOne(self, digits):
        n = len(digits)
        
        for i in range(n - 1, -1, -1):  # range(start, stop, step) is the pattern
            digits[i] += 1
            if digits[i] < 10:
                return digits
            digits[i] = 0  # carry over
        
        # If we exit the loop, it means all were 9s
        return [1] + digits #only runs when all the digits were 9s, or more generally, when the addition causes a carry that goes past the most significant digit

```
