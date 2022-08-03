# Given the API rand7() that generates a uniform random integer in the range [1, 7], write a function rand10() that generates a uniform random integer in the range [1, 10]. You can only call the API rand7(), and you shouldn't call any other API. Please do not use a language's built-in random API.

# Each test case will have one internal argument n, the number of times that your implemented function rand10() will be called while testing. Note that this is not an argument passed to rand10().

# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        v1 = rand7()
        while v1 > 5:
            v1 = rand7()
        print("v1 :", v1)
        
        v2 = rand7()
        while v2 == 7:
            v2 = rand7()
        print("v2 :", v2)
        
        if v2 < 4:
            return v1 
        else: 
            return v1 + 5
