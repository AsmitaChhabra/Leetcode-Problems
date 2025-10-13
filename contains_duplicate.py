class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # Step 1: Create an empty set to track seen numbers
        seen = set()
        
        # Step 2: Iterate through each number
        for num in nums:
            if num in seen:
                # Duplicate found
                return True
            seen.add(num)  # Add number to set
        
        # Step 3: No duplicates found
        return False
