'''
Author: yaojinxi 864554492@qq.com
Date: 2024-02-26 21:02:20
LastEditors: yaojinxi 864554492@qq.com
LastEditTime: 2024-02-26 21:22:33
FilePath: \leetcode\042\trap.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        all = 0
        leftMax = 0
        rightMax = 0
        print(left,height[right])
        while left < right:
            leftMax = max(leftMax, height[left])
            rightMax = max(rightMax, height[right])
            if(height[left] < height[right]):
                all += (leftMax - height[left])
                left += 1
            else:
                all += (rightMax - height[right])
                right -= 1
        return all



height: list =  [0,1,0,2,1,0,1,3,2,1,2,1] 
so = Solution()
print(so.trap(height))