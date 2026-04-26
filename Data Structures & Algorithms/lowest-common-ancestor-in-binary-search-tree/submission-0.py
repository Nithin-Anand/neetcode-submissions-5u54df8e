# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # DFS until you find p, maintain a stack of visited nodes, add p to stack
        # DFS until you find q, maintain a stack of visited nodes, add q to stack
        # Pop from longest until equal length until both nodes match

        p_nodes = self.dfs_with_visited_nodes(root, p, [])
        q_nodes = self.dfs_with_visited_nodes(root, q, [])

        while len(p_nodes) > len(q_nodes):
            p_nodes.pop()
        while len(q_nodes) > len(p_nodes):
            q_nodes.pop()

        while len(p_nodes) > 0:
            p_node_ancestor = p_nodes.pop()
            q_node_ancestor = q_nodes.pop()

            print(p_node_ancestor.val, q_node_ancestor.val)

            if p_node_ancestor.val == q_node_ancestor.val:
                return q_node_ancestor



    def dfs_with_visited_nodes(self, root: TreeNode, target: TreeNode, visited_nodes: list[TreeNode]):
        nodes = visited_nodes.copy()

        if root is None:
            return None

        nodes.append(root)
        if root.val == target.val:
            return nodes
        
        left_nodes = self.dfs_with_visited_nodes(root.left, target, nodes)
        right_nodes = self.dfs_with_visited_nodes(root.right, target, nodes)

        if left_nodes is not None:
            return left_nodes
        if right_nodes is not None:
            return right_nodes