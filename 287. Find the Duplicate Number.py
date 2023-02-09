# 287. Find the Duplicate Number

# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

# There is only one repeated number in nums, return this repeated number.

# You must solve the problem without modifying the array nums and uses only constant extra space.

 

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # for i in nums:
        #     cnt = (nums.count(i))
        #     print(cnt)
        #     ind = (nums.index(cnt))
        #     print(ind)
        # # if(cnt > 1) :
        # #     return(nums[ind])

            low = 0
            high = len(nums) - 1
            mid = (high + low) // 2
            while high > low :
                count = 0
                for k in nums:
                    if mid < k <= high:
                        count += 1
                if count > high - mid:
                    low = mid +1
                else:
                    high = mid
                mid = (high + low) // 2
                print(low, mid, high)
            return high






Example 1:
Input: nums = [1,3,4,2,2]
Output: 2

Example 2:
Input: nums = [3,1,3,4,2]
Output: 3
 
 
