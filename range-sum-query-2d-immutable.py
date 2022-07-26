# Given a 2D matrix matrix, handle multiple queries of the following type:

# Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
# Implement the NumMatrix class:

# NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
# int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

from typing import List

mat = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        return matrix
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        

# Your NumMatrix object will be instantiated and called as such:
if __name__ == '__main__':
    obj = NumMatrix(matrix=mat)
    param_1 = obj.sumRegion(row1,col1,row2,col2)