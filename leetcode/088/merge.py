'''
Author: yaojinxi 864554492@qq.com
Date: 2024-02-25 15:55:22
LastEditors: yaojinxi 864554492@qq.com
LastEditTime: 2024-02-25 16:13:50
FilePath: \leetcode\088\merge.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        leftIndex: int = m - 1
        rightIndex: int = n - 1
        checkIndex: int = m + n - 1
        while leftIndex >=0 and rightIndex >=0 :
            if nums1[leftIndex] >= nums2[rightIndex]:
                nums1[checkIndex] = nums1[leftIndex]
                leftIndex -= 1
                
            else :
                nums1[checkIndex] = nums2[rightIndex]
                rightIndex -= 1
                
            checkIndex -= 1
            
        while rightIndex >= 0 :
            nums1[checkIndex] = nums2[rightIndex]
            rightIndex -= 1
            checkIndex -= 1
            
        print(nums1)
        

nums1: list = [1,2,3,4,4,2]
nums2: list = [1,2,3,5]
m: int = 2
n: int = 3
so = Solution()

print(so.merge(nums1,m,nums2,n))