# Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.

from typing import List

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0]) -1

        print("length", m, n)

        count = 0

        for i in range(0,m):
            for j in range(n,-1,-1):
                if grid[i][j] < 0:
                    count += 1
        return count
        


if __name__ == '__main__':
    grid = [[5,1,0],[-5,-5,-5]]
    ob = Solution()
    res = ob.countNegatives(grid)
    print(res)