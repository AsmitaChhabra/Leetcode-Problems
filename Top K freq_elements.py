from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)              # Step 1: Count frequencies
        return [num for num, freq in count.most_common(k)]  # Step 2: Take top k
