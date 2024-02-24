'''
Author: yaojinxi 864554492@qq.com
Date: 2024-02-24 21:20:49
LastEditors: yaojinxi 864554492@qq.com
LastEditTime: 2024-02-24 22:31:21
FilePath: \leetcode\001\twoSum.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
class Solution(object):
    def twoSum(self, nums, target):
        n = len(nums)
        for i in range(n):
            print(i)
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        
        return []

     
    
t = Solution()
num: int = 6
nums: list = [3,2,4]

print(t.twoSum(nums,num))