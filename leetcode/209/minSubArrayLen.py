'''
Author: yaojinxi 864554492@qq.com
Date: 2024-09-11 14:33:26
LastEditors: yaojinxi 864554492@qq.com
LastEditTime: 2024-09-13 14:26:14
FilePath: \leetcode\209\minSubArrayLen.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
'''
Author: yaojinxi 864554492@qq.com
Date: 2024-09-11 14:33:26
LastEditors: yaojinxi 864554492@qq.com
LastEditTime: 2024-09-12 11:33:06
FilePath: \leetcode\209\minSubArrayLen.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
'''
Author: yaojinxi 864554492@qq.com
Date: 2024-09-11 14:33:26
LastEditors: yaojinxi 864554492@qq.com
LastEditTime: 2024-09-12 10:34:08
FilePath: \leetcode\209\minSubArrayLen.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        leng = len(nums)
        left = 0
        right = 0
        res = leng + 1
        total = 0
        while right < leng:
            total += nums[right]
            
            while total >= target:
                res = min(res,right - left + 1)
                total -= nums[left]
                left += 1
            right += 1
        if res == leng + 1: 
            return 0
        
        return res
        
target = 7 
nums = [2,3,1,2,4,3]
so = Solution()
result = so.minSubArrayLen(target,nums)
print(result)