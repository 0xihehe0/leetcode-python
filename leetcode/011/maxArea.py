
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left:int = 0
        right:int = len(height) - 1
        allArea:int = 0
        print(left , right)
        while left < right:
            nowArea = min(height[left], height[right]) * (right - left)
            allArea = max(nowArea,allArea)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return allArea


height: list = [1,8,6,2,5,4,8,3,7]

so = Solution()
so.maxArea(height)