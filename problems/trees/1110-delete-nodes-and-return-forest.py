from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        res_set = set([root])
        to_delete = set(to_delete)

        def dfs(node):
            if node is None:
                return

            res = node
            if node.val in to_delete:
                res_set.discard(node)
                res = None
                if node.right:
                    res_set.add(node.right)
                if node.left:
                    res_set.add(node.left)

            node.right = dfs(node.right)
            node.left = dfs(node.left)

            return res

        dfs(root)
        return list(res_set)
