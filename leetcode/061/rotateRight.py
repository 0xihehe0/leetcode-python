'''
Author: yaojinxi 864554492@qq.com
Date: 2024-09-01 15:51:23
LastEditors: yaojinxi 864554492@qq.com
LastEditTime: 2024-09-01 16:57:33
FilePath: \leetcode\061\rotateRight.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from typing import Optional  # Import Optional from the typing module
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
# Initialize each node
# Initialize each node
list1 = ListNode(1)
n1 = ListNode(4)
n2 = ListNode(1)

# Build references between nodes
list1.next = n1
n1.next = n2

value = 4

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        length = 0
        cur = head
        tail = None
        while cur:
            length += 1
            tail = cur
            cur = cur.next
        k = k % length
        if k == 0:
            return head
        k = length - k
        cur = head
        for i in range(k - 1):
            cur = cur.next
        new_head = cur.next
        tail.next = head
        cur.next = None
        return new_head
    
so = Solution()
so.rotateRight(list1,value)