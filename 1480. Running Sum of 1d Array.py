# 1480. Running Sum of 1d Array

# Problem : Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

# Return the running sum of nums.


# =================================
# l = [1,2,3,4,5]
# add = 0
# output = []
# for i in l :
#     add = add + i
#     output.append(add)

# print(output)
# =================================


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        add = 0
        output = []

        for i in nums :
            add = add + i
            output.append(add)

        return (output) 



# Example 1:
# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

# Example 2:
# Input: nums = [1,1,1,1,1]
# Output: [1,2,3,4,5]
# Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].

# Example 3:
# Input: nums = [3,1,2,10,1]
# Output: [3,4,6,16,17]