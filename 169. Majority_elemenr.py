136. Single Number
    
Problem : Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
    
    # solution 1 =========

class Solution(object):
    def majorityElement1(self, nums):
        nums.sort()
        return nums[len(nums)//2]

    # solution 2 =========

    def majorityElement2(self, nums):
        m = {}
        for n in nums:
            m[n] = m.get(n, 0) + 1
            if m[n] > len(nums)//2:
                return n

    # solution 3 =========

    def majorityElement(self, nums):
        candidate, count = nums[0], 0
        for num in nums:
            if num == candidate:
                count += 1
            elif count == 0:
                candidate, count = num, 1
            else:
                count -= 1
        return candidate

# Example 1:
# Input: nums = [3,2,3]
# Output: 3


# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
