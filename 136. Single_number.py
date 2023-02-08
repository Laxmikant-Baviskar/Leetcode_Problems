# Leetcode 136. Single Number

# Problem : Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.



class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
    # solution 1 =========
        # xor = 0
        # for num in nums:
        #     xor ^= num
        
        # return xor


    # solution 2 =========
        return reduce(lambda total, el: total ^ el, nums)


# Example 1:
# Input: nums = [2,2,1]
# Output: 1

# Example 2:
# Input: nums = [4,1,2,1,2]
# Output: 4

# Example 3:
# Input: nums = [1]
# Output: 1

