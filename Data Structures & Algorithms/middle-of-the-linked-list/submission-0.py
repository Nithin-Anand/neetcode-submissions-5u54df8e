# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0

        current_node = head
        while current_node is not None:
            length += 1
            current_node = current_node.next
        
        middle = (length // 2) + 1

        current_node = head
        for i in range(middle - 1):
            current_node = current_node.next
        
        return current_node

        