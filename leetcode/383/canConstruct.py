'''
Author: yaojinxi 864554492@qq.com
Date: 2024-09-01 20:39:15
LastEditors: yaojinxi 864554492@qq.com
LastEditTime: 2024-09-01 21:12:49
FilePath: \leetcode\383\canConstruct.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        majorMap: dict = {}
        count = 1
        for value in ransomNote:
            if value in majorMap:
                majorMap[value] += 1
            else:
                majorMap[value] = count
                
        for value in magazine:
            if value in majorMap:
                majorMap[value] -= 1
        
        for key, val in majorMap.items():   
            if val > 0:
                return False
            
        return True
                
ransomNote = "aa"
magazine = "ab"

so = Solution()

print(so.canConstruct(ransomNote,magazine))