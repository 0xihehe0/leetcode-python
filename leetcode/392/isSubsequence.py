'''
Author: yaojinxi 864554492@qq.com
Date: 2024-09-05 15:18:23
LastEditors: yaojinxi 864554492@qq.com
LastEditTime: 2024-09-06 12:06:17
FilePath: \leetcode\392\isSubsequence.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''

# "My approach is to initialize two pointers, index1 and index2, 
# and then traverse the string t. index1 will follow the string t, 
# and index2 will follow the string s. When the character at index1 in t is equal to the character at index2 in s, index2 will increment by 1.

# If index2 reaches the length of the string s, return True; otherwise, return False."

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index1 = 0
        index2 = 0
        if len(s) == 0:
            return True
        
        while len(t) > index1:
            if t[index1] == s[index2] : 
                index2 +=1
                if index2 == len(s):
                    return True
            index1 +=1
        return False
    
so = Solution()
s = ""
t = "ahbgdc"
result = so.isSubsequence(s,t)
print(result)