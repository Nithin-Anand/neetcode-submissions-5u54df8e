# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        import collections 
        visit_queue = collections.deque()
        result = []

        if root is None:
            return result
        
        visit_queue.append((root, 1))

        while visit_queue:
            current_node, depth = visit_queue.popleft()
            if depth == len(result):
                result[-1].append(current_node.val)
            else:
                result.append([current_node.val])
            
            if current_node.left is not None:
                visit_queue.append((current_node.left, depth+1))
            if current_node.right is not None:
                visit_queue.append((current_node.right, depth+1))
        
        return result

    