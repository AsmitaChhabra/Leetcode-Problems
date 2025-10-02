# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
# A subarray is a contiguous non-empty sequence of elements within an array.

python 
class Solution(object):
    def subarraySum(self, nums, k):
        count_of_array = 0   # total subarrays found
        prefix_sum = 0       # running sum
        hashmap = {0:1}      # seen sum 0 once at start
        
        for num in nums:
            prefix_sum += num
            
            if (prefix_sum - k) in hashmap:
                count_of_array += hashmap[prefix_sum - k]

            # update hashmap with current prefix_sum
            hashmap[prefix_sum] = hashmap.get(prefix_sum, 0) + 1

        return count_of_array
