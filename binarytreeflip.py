# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def DFS(root):
            if not root :
                return 
            DFS(root.left)
            DFS(root.right)
            root.left,root.right = root.right,root.left
        DFS(root)
        return root        