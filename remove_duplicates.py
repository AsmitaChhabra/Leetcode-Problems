class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # If the array is empty, return 0
        if not nums:
            return 0

        # i is the slow pointer (position of last unique element)
        i = 0

        # j is the fast pointer (current element being checked)
        for j in range(1, len(nums)):
            # If we find a new unique number
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]  # Move it to the next unique position

        # Return the count of unique elements
        return i + 1
