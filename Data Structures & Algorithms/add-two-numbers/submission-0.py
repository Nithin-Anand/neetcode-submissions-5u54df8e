# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry = 0

        current_l1 = l1
        current_l2 = l2

        result_head = None
        current_result = None

        while current_l1 is not None and current_l2 is not None:
            val = current_l1.val + current_l2.val + carry
            if val > 9:
                val = val % 10
                carry = 1
            else:
                carry = 0
                
            new_node = ListNode(val=val)
            if result_head is None:
                result_head = new_node
                current_result = result_head
            else:
                current_result.next = new_node
                current_result = current_result.next
            
            current_l1 = current_l1.next
            current_l2 = current_l2.next
        
        while current_l1 is not None and current_l2 is None:
            val = current_l1.val + carry
            if val > 9:
                val = val % 10
                carry = 1
            else:
                carry = 0
            new_node = ListNode(val)
            if result_head is None:
                result_head = new_node
                current_result = result_head
            else:
                current_result.next = new_node
                current_result = current_result.next
            
            current_l1 = current_l1.next
        
        while current_l1 is None and current_l2 is not None:
            val = current_l2.val + carry
            if val > 9:
                val = val % 10
                carry = 1
            else:
                carry = 0
            new_node = ListNode(val)
            if result_head is None:
                result_head = new_node
                current_result = result_head
            else:
                current_result.next = new_node
                current_result = current_result.next
            
            current_l2 = current_l2.next

        if carry == 1:
            current_result.next = ListNode(val=1)
        
        return result_head
        
            
