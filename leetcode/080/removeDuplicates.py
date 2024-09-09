
# "I will use a two-pointer approach to resolve the problem.

# Step 1:
# I initialize two variables, index and occurrence, both set to 1. Then, we start traversing the input nums array from index 1 to the end.

# Step 2:
# If nums[i] is equal to nums[i - 1], increment the occurrence by 1. Otherwise, reset occurrence to 1.

# Step 3:
# If occurrence is less than or equal to 2, set nums[index] to nums[i], and then increment index by 1.

# Step 4:
# Finally, return the index."

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 1
        occurance = 1
        
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                occurance += 1
            else:
                occurance = 1
                
            if occurance <= 2:
                nums[index] = nums[i]
                index += 1
            
        return index
        
        
nums = [1,1,1,2,2,3]
so = Solution()
result = so.removeDuplicates(nums)
print(result)
