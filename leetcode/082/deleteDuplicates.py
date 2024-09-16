'''
Author: yaojinxi 864554492@qq.com
Date: 2024-09-16 10:52:04
LastEditors: yaojinxi 864554492@qq.com
LastEditTime: 2024-09-16 10:52:18
FilePath: \leetcode\082\deleteDuplicates.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from typing import Optional  # Import Optional from the typing module

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return


list1 = ListNode(1)
n1 = ListNode(4)
n2 = ListNode(7)
n3 = ListNode(2)
n4 = ListNode(2)

list1.next = n1
n1.next = n2
n2.next = n3
n3.next = n4

so = Solution()

result = so.deleteDuplicates(list1)
print(result)