'''
Author: yaojinxi 864554492@qq.com
Date: 2024-08-27 20:25:44
LastEditors: yaojinxi 864554492@qq.com
LastEditTime: 2024-08-28 23:54:59
FilePath: \leetcode\203\removeElements.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from typing import Optional  # Import Optional from the typing module
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

value = 4
list1 = ListNode(1)
n1 = ListNode(4)
n2 = ListNode(4)
n3 = ListNode(7)

list1.next = n1
n1.next = n2
n2.next = n3

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        res = ListNode(0)
        res.next = head
        dummy = res
        curr = head
        while curr:
            if curr.val == val:
                dummy.next = curr.next
            else:
                dummy = curr 
            curr = curr.next
        return dummy.next
    
so = Solution()
so.removeElements(list1, value)