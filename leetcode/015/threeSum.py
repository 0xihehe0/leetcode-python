'''
Author: yaojinxi 864554492@qq.com
Date: 2024-09-06 19:52:57
LastEditors: yaojinxi 864554492@qq.com
LastEditTime: 2024-09-07 16:14:43
FilePath: \leetcode\015\threeSum.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortNums = sorted(nums)
       
        res = []
        for i in range(len(sortNums)):
            if i > 0 and sortNums[i] == sortNums[i-1]:
                continue
            print(i)
            j = i + 1
            k = len(nums) - 1
            
            while j < k:
                total = sortNums[i] + sortNums[j] + sortNums[k]
                if total < 0:
                    j += 1
                elif total > 0:
                    k -= 1
                else:
                    res.append([sortNums[i] , sortNums[j] , sortNums[k]])
                    j += 1
                    
                    while sortNums[j] == sortNums[j - 1] and j < k:
                        j += 1
        return res
    
nums = [-1,0,1,2,-1,-4]
so = Solution()
result = so.threeSum(nums)
print(result)