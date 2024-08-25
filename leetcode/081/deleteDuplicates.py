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
        print(head.next.val)
        return
    
so = Solution()
so.deleteDuplicates(list1)