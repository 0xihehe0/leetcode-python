from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        leng = len(nums)
        left = 0
        right = 0
        res = leng + 1
        total = 0
        while right < leng:
            total += nums[right]
            
            while total >= target:
                res = min(res,right - left + 1)
                total -= nums[left]
                left += 1
            right += 1
        if res == leng + 1: 
            return 0
        
        return res
        
target = 7 
nums = [2,3,1,2,4,3]
so = Solution()
result = so.minSubArrayLen(target,nums)
print(result)