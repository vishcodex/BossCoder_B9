# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.


from typing import List

from numpy import mat


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        row = []
        column = []

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row.append(i)
                    column.append(j)

        for i in range(m):
            for j in range(n):
                if i in row or j in column:
                    matrix[i][j] = 0

        print(matrix)

if __name__ == '__main__':
    mat = [[1,1,1],[1,0,1],[1,1,1]]
    ob = Solution()
    ob.setZeroes(mat)