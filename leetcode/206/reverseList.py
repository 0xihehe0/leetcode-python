'''
Author: yaojinxi 864554492@qq.com
Date: 2024-08-29 11:28:04
LastEditors: yaojinxi 864554492@qq.com
LastEditTime: 2024-08-29 12:27:53
FilePath: \leetcode\206\reverseList.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from typing import Optional  # Import Optional from the typing module
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
list1 = ListNode(1)
n1 = ListNode(4)
n2 = ListNode(7)

list1.next = n1
n1.next = n2

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = ListNode(0)
        nex = None

        while head:
            prev = head.next
            head.next = nex
            nex = head
            head = prev
            
        return nex
    
    def reverseList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return
    
        
so = Solution()
so.reverseList(list1)
so.reverseList2(list1)