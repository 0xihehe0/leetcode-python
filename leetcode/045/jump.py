# step1:
# First of all,we initialize three variates is near and far and jumpIndex,

# the first jump ,the near position should be nums[0],through the value,we can guarantee the jump range is "the value to the value -1"

# so,the far position should be 

# and add + 1 to jumpIndex.

# we compara the maximum of every jump ,and repeat the operation,finally we return the jumpIndex value.

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