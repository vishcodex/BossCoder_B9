# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.

from typing import List

mat = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
tgt = 5

def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    # Brute Force Approach
    # for top in range(len(matrix)):
    #     for left in range(len(matrix[0])):
    #         if matrix[top][left] == target:
    #             return True

    # Optimal Approch

    row = 0
    column = len(matrix[0])-1
    while(row<len(matrix) and column >=0):
        if matrix[row][column] > target :
            column -= 1
        elif matrix[row][column] < target :
            row += 1
        else:
            return True
    return False




a = searchMatrix(matrix=mat,target=tgt)
print(a)