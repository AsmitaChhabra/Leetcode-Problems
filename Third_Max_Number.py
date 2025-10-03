# LeetCode Problem #414: Third Maximum Number
# Given an integer array nums, return the third distinct maximum number in this array.
# If the third maximum does not exist, return the maximum number.

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Initialize three variables to track the top 3 distinct maximum numbers
        first = second = third = None

        # Loop through each number in the input array
        for num in nums:
            # Skip this number if it is already counted in first, second, or third
            if num == first or num == second or num == third:
                continue

            # If the number is larger than the current first maximum
            if first is None or num > first:
                # Shift previous maximums down
                third = second
                second = first
                first = num
            # If the number is larger than the second maximum
            elif second is None or num > second:
                # Shift second maximum down to third
                third = second
                second = num
            # If the number is larger than the third maximum
            elif third is None or num > third:
                third = num

        # If third maximum exists, return it; otherwise, return the maximum (first)
        return third if third is not None else first
