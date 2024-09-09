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
