from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = 0

        def inorder(root: Optional[TreeNode]):
            nonlocal k, res

            if(not root): return

            inorder(root.left)

            k -= 1
            if(k == 0):
                res = root.val
                return

            inorder(root.right)

        inorder(root)

        return res

