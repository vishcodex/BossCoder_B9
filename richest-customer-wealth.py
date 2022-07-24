# You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.

# A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.

from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        # n = len(accounts)
        # m = len(accounts[0])

        val = 0

        for i in accounts:
           if(sum(i) >= val):
            val = sum(i)
            return val


        # for i in range(n):
        #     tot = 0
        #     for j in range(m):
        #         # print(i,j)
        #         tot += accounts[i][j]
        #         total_sum.append(tot)


        # return max(total_sum)

if __name__ == '__main__':
    val = [[1,2,3],[3,2,1]]
    ob = Solution()
    res = ob.maximumWealth(val)
    print(res)