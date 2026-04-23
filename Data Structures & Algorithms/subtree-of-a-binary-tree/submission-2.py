# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        recursionStack = []

        recursionStack.append(root)
        
        while recursionStack:
            current = recursionStack.pop()
            if current is None:
                continue
            if self.isSameTree(current, subRoot):
                return True
            else:
                recursionStack.append(current.left)
                recursionStack.append(current.right)
        
        return False

        
    def isSameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None and subRoot is None:
            return True
        if (root is None and subRoot is not None) or (root is not None and subRoot is None):
            return False
        if root.val == subRoot.val:
            return self.isSameTree(root.left, subRoot.left) and self.isSameTree(root.right,subRoot.right)
