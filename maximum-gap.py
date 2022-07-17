# Given an integer array nums, return the maximum difference between two successive elements in its sorted form. If the array contains less than two elements, return 0.

# You must write an algorithm that runs in linear time and uses linear extra space.


from typing import List


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        val = sorted(nums)
        max_val_array = []
        for i in range(len(val)-1):
            # print(val[i], val[i+1])
            max_val_array.append(abs(val[i] - val[i+1]))
        return max(max_val_array)

if __name__ == '__main__':
    ob = Solution()
    res = ob.maximumGap([3,2])
    print(res)