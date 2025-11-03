class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n  # handle cases where k > n

        # Step 1: reverse the whole array
        nums.reverse()

        # Step 2: reverse the first k elements
        nums[:k] = reversed(nums[:k])

        # Step 3: reverse the remaining n-k elements
        nums[k:] = reversed(nums[k:])
