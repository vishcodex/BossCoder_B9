# A self-dividing number is a number that is divisible by every digit it contains.

# For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
# A self-dividing number is not allowed to contain the digit zero.

# Given two integers left and right, return a list of all the self-dividing numbers in the range [left, right].

from typing import List

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for n in range(left, right+1):
            digits = set(map(int, str(n)))       
            if 0 in digits: continue             
                    
            if all(n % d == 0 for d in digits):  
                res.append(n)             
        return res

        


if __name__ == '__main__':
    l, r = 1, 22
    ob = Solution()
    res = ob.selfDividingNumbers(l, r)
    print(res)