'''
Author: yaojinxi 864554492@qq.com
Date: 2024-03-06 17:20:57
LastEditors: yaojinxi 864554492@qq.com
LastEditTime: 2024-03-06 17:33:22
FilePath: \leetcode\039\combinationSum.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
class Solution(object):
    def combinationSum(self, candidates, target):
        start = 0
        resList = []
        checkList = []
        candidates.sort()
        self.combine(resList, candidates, target, start, checkList)
        return resList
        
    def combine(self,resList, candidates, target, start, checkList):
        if(target == 0):
            resList.append(list(checkList))
            return 
        
        for i in range(start, len(candidates)):
            choice = candidates[i]
            if(target - choice < 0):
                break
            
            checkList.append(choice)
            self.combine(resList, candidates, target - choice, i, checkList)
            checkList.pop()
            
        
candidates = [8,7,4,3]
target = 11
so = Solution()
print(so.combinationSum(candidates, target))