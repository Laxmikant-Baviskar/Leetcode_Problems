283. Move Zeroes

problem : Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

# ==========================================
# l = [0 , 1]
# l.sort()
# print(l)

# def moveZeroes(nums):
#     nums.sort()
#     for i in range (len(nums)):
#         if nums[i] == 0 :
#             del nums[i]
#             nums.append(0)
        
#     # print(nums)
#     return nums 

# nums = [0,1,0,3,12]
# # nums = [0 , 1]
# print(moveZeroes(nums))

# ==========================================

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # nums.sort()
        # for i in range (len(nums)) :
        #     if nums[i] == 0 :
        #         del nums[i]
        #         nums.append(0)
                
        # print(nums)nums.sort()

        # for i in  nums :
        #     if i == 0 :
        #         del nums[i]
        #         nums.append(0)
        #     elif 
        #         nums.reverse()
                
        # print(nums)

        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1


# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Example 2:
# Input: nums = [0]
# Output: [0]

# Example 3:
# Input: nums = [0 , 1]
# Output: [1 , 0]