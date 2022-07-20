# Given an array, return the length of the longest subarray of non-negative integers

# Examples : 

# Input : {2, 3, 4, -1, -2, 1, 5, 6, 3}
# Output : 4

# The subarray [ 1, 5, 6, 3] has length 4 and 
# contains no negative integers

# Input : {1, 0, 0, 1, -1, -1, 0, 0, 1, 0}
# Output : 4

# Subarrays [1, 0, 0, 1] and [0, 0, 1, 0] have 
# equal lengths but sum of first one is greater
# so that will be the output.

from typing import List

class Solution:
    def longest_sub_non_neg_array(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        for i in range(n):
            curr = 0
            while i < n and nums[i] >= 0:
                curr += 1
                i += 1
            res = max(res, curr)
        return res

if __name__ == '__main__':
    ob = Solution()
    r = ob.longest_sub_non_neg_array([1, 0, 4, 0, 1, -1, -1, 0, 0, 1, 0])
    print(r)

