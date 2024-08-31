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
n3 = ListNode(7)

# Build references between nodes
list1.next = n1
n1.next = n2
n2.next = n3

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return
    
so = Solution()
so.swapPairs(list1)