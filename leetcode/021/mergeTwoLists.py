'''
Author: yaojinxi 864554492@qq.com
Date: 2024-08-25 13:57:03
LastEditors: yaojinxi 864554492@qq.com
LastEditTime: 2024-08-25 15:29:51
FilePath: \leetcode\021\mergeTwoLists.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
# Definition for singly-linked list.
from typing import Optional  # Import Optional from the typing module
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
# Initialize each node
# Initialize each node
list1 = ListNode(1)
n1 = ListNode(4)
n2 = ListNode(7)

list2 = ListNode(5)
n4 = ListNode(6)

# Build references between nodes
list1.next = n1
n1.next = n2

list2.next = n4
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                res.next = list1
                list1, res = list1.next, list1
            else:
                res.next = list2
                list2,res = list2.next, list2
        
        if list1 or list2:
            res.next = list1 if list1 else list2
            
        return dummy.next



so = Solution()
so.mergeTwoLists(list1, list2)