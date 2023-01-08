class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # for i in range len(nums) :
        #     if i == x:
        #         return True
        #     else :
        #         return false

        return len(nums) != len(set(nums))


# Example 1:

# Input: nums = [1,2,3,1]
# Output: true
# Example 2:

# Input: nums = [1,2,3,4]
# Output: false
# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true