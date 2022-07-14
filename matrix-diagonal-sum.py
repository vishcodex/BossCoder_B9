# Given a square matrix mat, return the sum of the matrix diagonals.

# Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.

 

# Example 1:


# Input: mat = [[1,2,3],
#               [4,5,6],
#               [7,8,9]]
# Output: 25
# Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
# Notice that element mat[1][1] = 5 is counted only once.

from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sums=0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if(i==j):
                    sums+=mat[i][j]
        mat[i]=mat[i][::-1]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if(i==j):
                    sums+=mat[i][j]
        if(len(mat)%2 != 0):
            sums-=mat[len(mat)//2][len(mat)//2]
        return sums
                    

if __name__ == '__main__':

    mat_val = [[1,2,3],
              [4,5,6],
              [7,8,9]]
    ob = Solution()
    res = ob.diagonalSum(mat=mat_val)
    print(res)