

# Code
```python3 []
class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Reverse the list of characters s in-place.
        Do not return anything — modify s directly.
        Time complexity: O(n) where n = len(s)
        Space complexity: O(1) extra memory (only a few variables)
        """

        # 1) Initialize two pointers:
        #    left  -> starts at the beginning (index 0)
        #    right -> starts at the end   (last index = len(s) - 1)
        left, right = 0, len(s) - 1

        # 2) Continue swapping while left pointer is before right pointer.
        #    When left >= right we've reached the middle (done).
        while left < right:
            # -------------------------
            # SWAP step (single-line Python swap)
            # s[left], s[right] = s[right], s[left]
            #
            # Left side (assignment targets):  s[left], s[right]
            # Right side (values to assign):  s[right], s[left]
            #
            # Python evaluates the right side first (reads the two values),
            # then assigns them into the left side positions simultaneously.
            # This performs an in-place swap without a temporary variable.
            # -------------------------
            s[left], s[right] = s[right], s[left]

            # After swapping the characters at left and right, move pointers inward:
            # - left moves one step to the right (toward middle)
            # - right moves one step to the left (toward middle)
            left += 1
            right -= 1

        # When the loop ends, all characters have been swapped pairwise and
        # the list s is reversed in-place.

```
