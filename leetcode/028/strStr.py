'''
Author: yaojinxi 864554492@qq.com
Date: 2024-09-12 13:05:01
LastEditors: yaojinxi 864554492@qq.com
LastEditTime: 2024-09-12 14:11:57
FilePath: \leetcode\028\strStr.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''

# "My method is to extract the substring from the 
# current index with the length of the needle in each iteration of the loop. 
# If the substring matches the needle, I return the current index."


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        length = len(needle)
        fristIndex = needle[0:1]
        for i in range(len(haystack)):
            if haystack[i] == fristIndex and needle == haystack[i:length + i]:
                return i
        return -1
        
        
haystack = "sabbutsad"
needle = "sad"
so = Solution()
result = so.strStr(haystack, needle)
print(result)