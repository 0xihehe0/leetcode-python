'''
Author: yaojinxi 864554492@qq.com
Date: 2024-02-26 20:36:01
LastEditors: yaojinxi 864554492@qq.com
LastEditTime: 2024-09-06 19:45:13
FilePath: \leetcode\011\maxArea.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''

from typing import List

# step1:
# I will initialize two pointers, left and right.
# the left pointer will start at the 0 index,
# the right pointer will start an the array last minus1 index

# step2:
# i will caculate left value times right value and save this value, 
# throught every caculate total then get one maximum and return it.

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