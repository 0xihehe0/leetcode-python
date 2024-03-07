'''
Author: yaojinxi 864554492@qq.com
Date: 2024-03-07 20:16:46
LastEditors: yaojinxi 864554492@qq.com
LastEditTime: 2024-03-07 20:29:09
FilePath: \leetcode\071\simplifyPath.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
class Solution:
    def simplifyPath(self, path: str) -> str:
        strArr:list = path.split("/")
        stack = []
        for i in range(len(strArr)):
            value = strArr[i]
            if value == "..":
                if stack:
                    stack.pop()
            elif value != "." and value:
                stack.append(value)
        
        return "/" + "/".join(stack)
        
path = "/a/./b/../../c/"
so = Solution()
print(so.simplifyPath(path))