# Given an integer number n, return the difference between the product of its digits and the sum of its digits.

class Solution:
    def subtractProductAndSum(self, n: int) -> int:

        # m = 1
        # s = 0

        # for i in str(n):
        #     m = m * int(i)
        #     s = int(s) + int(i)

        # return m - s     


        # Solution using RECURSION

            # """This is a recursive function
            # to find the factorial of an integer"""
            # def sumOfDigits(x):
            #     lastDigit = 0
            #     leftNumber = 0
            #     if n == 0:
            #         return 0
            #     else:
            #         lastDigit = n % 10
            #         leftNumber = n // 10
            #         return (lastDigit + sumOfDigits(leftNumber))




if __name__ == '__main__':
    n = 234
    ob = Solution()
    res = ob.subtractProductAndSum(n)
    print(res)
