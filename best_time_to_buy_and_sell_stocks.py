
# Code
```python3 []
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')  # start with a huge number
        max_profit = 0            # start with no profit

        for price in prices:
            # update min_price if we find a lower price
            if price < min_price:
                min_price = price
            # check profit if sold today
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit

```
