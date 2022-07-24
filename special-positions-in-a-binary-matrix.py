# Given an m x n binary matrix mat, return the number of special positions in mat.

# A position (i, j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed).

from typing import List

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        n = len(mat)
        m = len(mat[0])

        x_list = [0]*n
        y_list = [0]*m

        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1:
                    x_list[i] += 1
                    y_list[j] += 1

        sum = 0
        for row in range(n):
            for col in range(m):
                if mat[row][col] == 1 and x_list[row] == 1 and y_list[col] == 1:
                    sum += 1
        return sum
        


if __name__ == '__main__':
    mat = [[1,0,0],[0,0,1],[1,0,0]]
    ob = Solution()
    res = ob.numSpecial(mat)
    print(res)