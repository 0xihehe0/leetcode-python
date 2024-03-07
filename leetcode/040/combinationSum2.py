'''
Author: yaojinxi 864554492@qq.com
Date: 2024-03-07 16:36:26
LastEditors: yaojinxi 864554492@qq.com
LastEditTime: 2024-03-07 16:51:20
FilePath: \leetcode\040\combinationSum2.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''

from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        resList = []
        start = 0
        checkList = []
        candidates.sort()
        self.combin(resList,start,target,candidates,checkList)
        return resList
    def combin(self, resList,start,target,candidates,checkList):
        if target == 0:
            resList.append(list(checkList))
            return
        
        for i in range(start,len(candidates)):
            value = candidates[i]
            if(target - value < 0):
                break
            
            if(value == candidates[i - 1] and i > start):
                continue
            
            checkList.append(value)
            self.combin(resList,i + 1,target - value,candidates,checkList)
            checkList.pop()
            

candidates = [10,1,2,7,6,1,5]
target = 8
so = Solution()
print(so.combinationSum2(candidates, target))
