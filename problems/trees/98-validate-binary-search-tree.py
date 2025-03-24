from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        values = []

        def dfs(node):
            if not node:
                return
            
            # in-order traversal
            dfs(node.left)
            values.append(node.val)
            dfs(node.right)
        
        dfs(root)
        for i in range(len(values) - 1):
            if values[i] >= values[i + 1]:
                return False
        return True


class Solution2:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        def validate(node, left_bound, right_bound):
            if node is None:
                return True

            if not (left_bound < node.val < right_bound):
                return False

            return validate(node.left, left_bound, node.val) and validate(node.right, node.val, right_bound)

        return validate(root, float('-inf'), float('inf'))
