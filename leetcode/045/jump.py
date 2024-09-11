from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        far = 0
        near = 0
        jumpIndex = 0
        length = len(nums)
        while far < length - 1: 
            fastherst = 0
            for i in range(near,far + 1):
                fastherst = max(fastherst,i + nums[i])
                
            near = far + 1       
            far = fastherst
            jumpIndex += 1
        return jumpIndex
    
nums = [2,3,1,1,4]
so = Solution()
result = so.jump(nums)
print(result)