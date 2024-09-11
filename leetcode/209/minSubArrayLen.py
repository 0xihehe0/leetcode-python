from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 1
        while right < len(nums):
            print(left,right)
            if nums[left] or nums[right] == target:
                return 1
            
            if nums[left] + nums[right] == target:
                print(left,right)
            
            if nums[left] + nums[right] < target:
                right += 1
                
            if nums[left] + nums[right] > target:
                left += 1
                right += 1
                
        return
        
target = 7 
nums = [2,3,1,2,4,3]
so = Solution()
result = so.minSubArrayLen(target,nums)
print(result)