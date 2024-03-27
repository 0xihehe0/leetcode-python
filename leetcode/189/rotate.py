'''
Author: yaojinxi 864554492@qq.com
Date: 2024-03-27 22:38:55
LastEditors: yaojinxi 864554492@qq.com
LastEditTime: 2024-03-27 22:56:29
FilePath: \leetcode\189\rotate.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
class Solution:
    def rotate(self, nums, k) -> None:
        res = [0] * len(nums)
        for i in range(0,len(nums)):
            res[(i + k) % len(nums)] = nums[i]
        print(res)
        for i in range(0,len(nums)):
            nums[i] = res[i]
        


nums = [1,2,3,4,5,6,7]
k = 3

so = Solution()
so.rotate(nums, k)

