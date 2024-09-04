
from typing import List  # Import Optional from the typing module
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic: dict = {}
        for i in range(len(nums)):
            if nums[i] in dic and abs(i - dic[nums[i]]) <= k:
                return True
            dic[nums[i]] = i
            
        return False
    
so = Solution()
nums = [1,2,3,1]
k = 3
result = so.containsNearbyDuplicate(nums, k)
print(result)