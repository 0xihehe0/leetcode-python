'''
Author: yaojinxi 864554492@qq.com
Date: 2024-09-05 14:05:27
LastEditors: yaojinxi 864554492@qq.com
LastEditTime: 2024-09-05 14:41:18
FilePath: \leetcode\128\longestConsecutive.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from typing import List 

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        num_set = set(nums) 
        for n in nums:
            if n - 1 not in num_set:
                length = 1
                
                while n + length in num_set:
                    length += 1
                    
                longest = max(longest,length)

        return longest


so = Solution()
nums = [100,4,200,1,3,2]
result = so.longestConsecutive(nums)
print(result)