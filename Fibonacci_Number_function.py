Fibonacci Number function


# Code
```python3 []
class Solution:
    def fib(self, n: int) -> int:   # Name must be 'fib'
        if n == 0:
            return 0
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

```
