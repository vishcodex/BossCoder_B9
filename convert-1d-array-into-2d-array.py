# You are given a 0-indexed 1-dimensional (1D) integer array original, and two integers, m and n. You are tasked with creating a 2-dimensional (2D) array with m rows and n columns using all the elements from original.

# The elements from indices 0 to n - 1 (inclusive) of original should form the first row of the constructed 2D array, the elements from indices n to 2 * n - 1 (inclusive) should form the second row of the constructed 2D array, and so on.

# Return an m x n 2D array constructed according to the above procedure, or an empty 2D array if it is impossible.

from typing import List
 
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        
        if len(original)!=n*m: return []
        ans=[]
        for i in range(0,len(original),n): 
            # Logic is to use slicing
            # print("i, n, original[i:i+n] ",i, n, original[i:i+n])
            ans.append(original[i:i+n])
        return ans


if __name__ == '__main__':
    original = [1,2,3,4]
    m = 2
    n = 2
    ob = Solution()
    res = ob.construct2DArray(original, m , 2)
    print(res)
