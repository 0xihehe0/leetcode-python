'''
Author: yaojinxi 864554492@qq.com
Date: 2024-03-01 12:56:42
LastEditors: yaojinxi 864554492@qq.com
LastEditTime: 2024-03-01 14:37:24
FilePath: \leetcode\056\merge.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        checkArr:list = []
        check:list = intervals[0]
        for i in range(len(intervals)):
            value:list = intervals[i]
            print(check[1],value[0])
            if(check[1] >= value[0]):
                check[1] = max(check[1], value[1])
            else:
                checkArr.append(check)
                check = value
        
        checkArr.append(check)
        return checkArr
        
        
intervals =[
    [1, 2],
    [3, 6],
    [4, 7],
    [5, 8],
    [9, 10],
    [15, 18]
]
so = Solution()
print(so.merge(intervals))