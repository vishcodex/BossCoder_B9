# You are given an integer array arr of length n that represents a permutation of the integers in the range [0, n - 1].

# We split arr into some number of chunks (i.e., partitions), and individually sort each chunk. After concatenating them, the result should equal the sorted array.

# Return the largest number of chunks we can make to sort the array.

from typing import List 

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        count=0
        a=sorted(arr)
        h=[]
        for ele in range(len(arr)):
            print(sorted(arr[:ele]), sorted(arr[ele::]))
            h.extend(sorted(arr[:ele]))
            h.extend(sorted(arr[ele::]))
            print("h, a ",h, a)
            if(h==a):
                count+=1
            h=[]
        return count

        


if __name__ == '__main__':
    arr = [4,3,2,1,0]
    ob = Solution()
    res = ob.maxChunksToSorted(arr)
    print(res)