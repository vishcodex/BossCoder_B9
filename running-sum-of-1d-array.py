# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

# Return the running sum of nums.

from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        lis = []
        val = 0
        for i in nums:
            val = val + i
            lis.append(val)
        return lis




if __name__ == '__main__':
    val = [1,2,3,4]
    ob = Solution()
    res = ob.runningSum(val)
    print(res)