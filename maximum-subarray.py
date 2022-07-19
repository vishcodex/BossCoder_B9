# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# A subarray is a contiguous part of an array.

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        max_sum = nums[0]
        cur_sum = max_sum
        for i in range(1,n):
            cur_sum = max(nums[i] + cur_sum, nums[i])
            max_sum = max(cur_sum, max_sum)
        return max_sum
                

if __name__ == '__main__':
    ob = Solution()
    res = ob.maxSubArray([5,4,-1,7,8])
    print(res)