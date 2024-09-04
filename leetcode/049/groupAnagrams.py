'''
Author: yaojinxi 864554492@qq.com
Date: 2024-09-03 14:05:18
LastEditors: yaojinxi 864554492@qq.com
LastEditTime: 2024-09-04 18:05:33
FilePath: \leetcode\049\groupAnagrams.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE

'''
from typing import List  # Import Optional from the typing module
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs):
        anagram_map = defaultdict(list)
        
        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_map[sorted_word].append(word)
        
        return list(anagram_map.values())
    
so = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
result = so.groupAnagrams(strs)
print(result)