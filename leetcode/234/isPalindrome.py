'''
Author: yaojinxi 864554492@qq.com
Date: 2024-08-29 13:48:03
LastEditors: yaojinxi 864554492@qq.com
LastEditTime: 2024-08-29 14:20:52
FilePath: \leetcode\234\isPalindrome.py
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

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        return False
    
