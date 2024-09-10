'''
Author: yaojinxi 864554492@qq.com
Date: 2024-09-09 16:27:26
LastEditors: yaojinxi 864554492@qq.com
LastEditTime: 2024-09-10 23:13:15
FilePath: \leetcode\055\canJump.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        
        return True if goal == 0 else False

nums = [2,3,1,1,4]
so = Solution()
result = so.canJump(nums)
print(result)