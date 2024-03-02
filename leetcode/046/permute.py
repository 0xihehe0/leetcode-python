'''
Author: yaojinxi 864554492@qq.com
Date: 2024-03-02 16:34:02
LastEditors: yaojinxi 864554492@qq.com
LastEditTime: 2024-03-02 17:02:06
FilePath: \leetcode\046\permute.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        resList:list = []
        selectList:list = [False] * len(nums)
        checkList:list = []
        self.dfs(resList, selectList, checkList,nums)
        return resList
        
    def dfs(self,resList: list[int], selectList: list[bool], checkList: list[int], nums: list[list[int]]):
        if len(checkList) == len(nums):
            resList.append(list(checkList))
            return
        
        for i, choice in enumerate(nums):
            if not selectList[i]:
                selectList[i] = True
                checkList.append(choice)
                self.dfs(resList,selectList,checkList,nums)
                selectList[i] = False
                checkList.pop()
        return
        
nums:list = [1,2,3]
so = Solution()
print(so.permute(nums))