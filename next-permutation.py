# A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

# For example, for arr = [1,2,3], the following are considered permutations of arr: [1,2,3], [1,3,2], [3,1,2], [2,3,1].
# The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

# For example, the next permutation of arr = [1,2,3] is [1,3,2].
# Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
# While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
# Given an array of integers nums, find the next permutation of nums.

# The replacement must be in place and use only constant extra memory.

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
    
        for i in range(size-1, 0, -1):
            curr, prev = nums[i], nums[i-1]
            if curr > prev:
                # NOTE :- nums[i:] is already in decreasing order

                # 1. decide j := find the immediate next elem to `nums[i-1]`
                for j in range(size-1, i-1, -1):
                    if nums[j] > prev:
                        break

                # 2. Swap both
                nums[j], nums[i-1] = prev, nums[j]

                # NOTE :- now `nums[j:]` may be not in Decreasing order
                # 3. Recorrect the Disturbed Decreasing Order because of above Swapping
                #    !-> Disturbed Decreasing portion can lie in :- nums[j:]

                for k in range(j, size-1):
                    if nums[k] < nums[k+1]:
                        # buuble up 
                        nums[k], nums[k+1] = nums[k+1], nums[k]
                    else:
                        # Now the nums[j:] is in Decreasing order
                        break

                # 4. Reverse the Decreasing Part 
                #    NOTE :- this can be done in-place via 2 pointers 
                nums[i:] = nums[i:][::-1]

                # 5. Indicator of next permutation available
                break 
        else:
            # Next Perm is not available so reverse the entire array
            nums.reverse()