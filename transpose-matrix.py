# Given a 2D integer array matrix, return the transpose of matrix.

# The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

from typing import List 

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:

        # SOLUTION ONE

        
        return list(map(list, zip(*matrix)))

        # SOLUTION TWO
        # m, n = len(matrix), len(matrix[0])
        # transpose = []
        # for i in range(n):
        #     newRow = []
        #     for j in range(m):
        #         newRow.append(matrix[j][i])
        #     transpose.append(newRow)
            
        # return transpose
        


if __name__ == '__main__':
    mat = [[1,2,3],[4,5,6],[7,8,9]]
    ob = Solution()
    res = ob.transpose(mat)
    print(res)