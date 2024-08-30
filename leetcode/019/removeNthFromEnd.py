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

value = 1

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        res = ListNode(0, head)
        dummy = res
       
        for i in range(n):
           head = head.next
           
        while head:
            head = head.next
            dummy = dummy.next
            
        dummy.next =dummy.next.next       
        return res.next
    
so = Solution()
so.removeNthFromEnd(list1,value)