'''
Author: yaojinxi 864554492@qq.com
Date: 2024-09-02 16:47:58
LastEditors: yaojinxi 864554492@qq.com
LastEditTime: 2024-09-02 19:55:23
FilePath: \leetcode\290\wordPattern.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mapDic: dict = {}
        reverseMapDic: dict = {}
        sArray = s.split()
        
        # Check if lengths are equal
        if len(pattern) != len(sArray):
            return False
        
        for index, value in enumerate(pattern):
            word = sArray[index]
            
            if value in mapDic:
                if mapDic[value] != word:
                    return False
            else:
                if word in reverseMapDic:
                    return False
                mapDic[value] = word
                reverseMapDic[word] = value
        
        return True
    
so = Solution()
pattern = "abba"
s = "dog cat cat fish"
print(so.wordPattern(pattern,s))