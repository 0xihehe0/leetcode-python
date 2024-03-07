'''
Author: yaojinxi 864554492@qq.com
Date: 2024-03-07 17:36:34
LastEditors: yaojinxi 864554492@qq.com
LastEditTime: 2024-03-07 17:38:36
FilePath: \leetcode\070\climbStairs.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3,n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
            
        return dp[n]
    
n = 5
so = Solution()
print(so.climbStairs(n))