# In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.

# You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of the wanted reshaped matrix.

# The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.

# If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

from typing import List

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:

        # SOLUTION ONE

        # k = [j for i in mat for j in i]
        # d=[]
        
        # if r*c == len(k): 
            
        #     for i in range(0,len(k),c):
        #         d.append(k[i:i+c])
        #     return d
        # else:
        #     return mat

        mat_len = len(mat[0]) * len(mat)

        new_rows = [0]*r
        new_cols = [0]*c
        
        if r * c != mat_len:
            return mat

        row = []
        res = []

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                row.append(mat[i][j])
                if len(row) == c:
                    res.append(row)
                    row = []
        return res
                    


if __name__ == '__main__':
    mat,r,c = [[1,2],[3,4]],1,4
    ob = Solution()
    res = ob.matrixReshape(mat, r, c)
    print(res)