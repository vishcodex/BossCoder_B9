# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_val = height[0]
        left = [0]*n
        for i in range(0,n) :
            if left_val < height[i]:
                left_val = height[i]
                left[i] = left_val
            else:
                left[i] = left_val
        print("left :", left)

        right_val = height[-1]
        right = [0]*n
        for i in range(n-1, -1, -1):
            if right_val < height[i]:
                right_val = height[i]
                right[i] = right_val
            else:
                right[i] = right_val
        print("right :", right)

        res = 0
        for i in range(n):
            res += min(left[i],right[i]) - height[i]
        return res

if __name__ == '__main__':
    ob = Solution()
    res = ob.trap([1,0,2,0,1,0,3,1,0,2])
    print(res)
