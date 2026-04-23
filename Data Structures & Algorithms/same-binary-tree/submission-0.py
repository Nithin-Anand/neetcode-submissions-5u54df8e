# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections 
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_queue = collections.deque()
        q_queue = collections.deque()

        if p is None and q is None:
            return True
        if (p is None and q is not None) or (p is not None and q is None):
            return False

        p_queue.append(p)
        q_queue.append(q)

        while p_queue and q_queue:
            current_p = p_queue.popleft()
            current_q = q_queue.popleft()
        
            if current_p is None and current_q is None:
                continue

            if (current_p is None and current_q is not None) or (current_p is not None and current_q is None):
                return False

            if current_p.val != current_q.val:
                return False
            
            p_queue.append(current_p.left)
            p_queue.append(current_p.right)

            q_queue.append(current_q.left)
            q_queue.append(current_q.right)
            

        
        if not p_queue and q_queue:
            return False
        
        if not q_queue and p_queue:
            return False
        
        return True
