'''
Author: yaojinxi 864554492@qq.com
Date: 2024-09-08 13:58:13
LastEditors: yaojinxi 864554492@qq.com
LastEditTime: 2024-09-08 14:36:47
FilePath: \leetcode\026\removeDuplicates.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        low = 1
        fast = 1
        while fast < len(nums):
            if nums[fast] != nums[low - 1]:
                nums[low] = nums[fast]
                low += 1
            
            fast += 1
        return low
        
nums = [0,0,1,1,1,2,2,3,3,4]
so = Solution()
so.removeDuplicates(nums)