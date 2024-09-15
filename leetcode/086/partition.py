'''
Author: yaojinxi 864554492@qq.com
Date: 2024-09-15 14:38:45
LastEditors: yaojinxi 864554492@qq.com
LastEditTime: 2024-09-15 23:03:23
FilePath: \leetcode\086\partition.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from typing import Optional  # Import Optional from the typing module

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        slist = ListNode()
        blist = ListNode()
        small,big = slist,blist
        
        while head:
            if head.val < x:
                small.next = head
                small = small.next
                
            else:
                big.next = head
                big = big.next
                
            head = head.next
            
        small.next = blist.next
        big.next = None
        
        return slist.next
    
list1 = ListNode(1)
n1 = ListNode(4)
n2 = ListNode(7)
n3 = ListNode(2)
n4 = ListNode(2)

list1.next = n1
n1.next = n2
n2.next = n3
n3.next = n4

x = 3

so = Solution()
so.partition(list1,x)