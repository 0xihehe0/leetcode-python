'''
Author: yaojinxi 864554492@qq.com
Date: 2024-08-25 15:54:39
LastEditors: yaojinxi 864554492@qq.com
LastEditTime: 2024-08-26 22:36:00
FilePath: \leetcode\083\deleteDuplicates.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
# Definition for singly-linked list.
from typing import Optional  # Import Optional from the typing module

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
list1 = ListNode(1)
n1 = ListNode(4)
n2 = ListNode(7)        
n3 = ListNode(7) 
n4 = ListNode(10) 
n5 = ListNode(10)         
        
list1.next = n1
n1.next = n2
n2.next = n3     
n3.next = n4
n4.next = n5


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = head
        while head and head.next:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next 

        return res
    
so = Solution()
so.deleteDuplicates(list1)