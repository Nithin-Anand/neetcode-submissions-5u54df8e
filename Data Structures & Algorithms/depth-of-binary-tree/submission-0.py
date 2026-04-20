# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if root is [] or root is None:
            return 0

        queue = collections.deque()

        queue.append((root, 1))

        max_depth = 1

        while queue:
            current_node, current_depth = queue.popleft()
            if current_depth > max_depth:
                max_depth = current_depth

            if current_node.left is not None:
                queue.append((current_node.left, current_depth+1))
            if current_node.right is not None:
                queue.append((current_node.right, current_depth+1))
        
        return max_depth

            



