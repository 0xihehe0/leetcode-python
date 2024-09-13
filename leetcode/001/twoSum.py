'''
Author: yaojinxi 864554492@qq.com
Date: 2024-02-24 21:20:49
LastEditors: yaojinxi 864554492@qq.com
LastEditTime: 2024-09-12 20:16:37
FilePath: \leetcode\001\twoSum.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
class Solution(object):
    def twoSum(self, nums, target):
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
    
    def twoSum2(self, nums, target):
        numHash = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in numHash:
                return [numHash[complement], i]
            numHash[num] = i
        return []
    

# 测试代码
t = Solution()
nums = [3, 2, 4]
target = 6

print(t.twoSum(nums, target))
print(t.twoSum2(nums, target))