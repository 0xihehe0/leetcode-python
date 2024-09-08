'''
Author: yaojinxi 864554492@qq.com
Date: 2024-08-31 22:40:22
LastEditors: yaojinxi 864554492@qq.com
LastEditTime: 2024-09-08 13:54:54
FilePath: \leetcode\027\removeElement.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            print(i)
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        
        return k
    
nums = [3,2,2,3]
val = 3
so = Solution()
result = so.removeElement(nums,val)
print(result)