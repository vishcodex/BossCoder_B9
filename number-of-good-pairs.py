# Given an array of integers nums, return the number of good pairs.

# A pair (i, j) is called good if nums[i] == nums[j] and i < j.



from typing import List 

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # BRUTE FORCE APPROACH

        # count = 0
        # for i in range(0,len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] == nums[j]:
        #             count += 1
        # return count
        
        # OPTIMIZED using mathematical formulae

        # dic = {}
        # count = 0
        # for i in nums:
        #     if i not in dic:
        #         dic[i] = 1
        #     elif i in dic:
        #         dic[i] += 1
    

        # for key, value in dic.items():
        #     if value > 1:
        #         count += value * (value -1) // 2
        # return count

        # Hash map Solution

        goodpairs = {}
        counter = 0
        for i in nums:
            if i in goodpairs:
                counter+=goodpairs[i]
                goodpairs[i]+=1
            else:
                goodpairs[i]=1
        return counter


if __name__ == '__main__':
    nums = [1,2,3,1,1,3]
    ob = Solution()
    res = ob.numIdenticalPairs(nums)
    print(res)


