# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        def inorder(root,l=[]):
            if not root:
                return
            if root.left:
                 inorder(root.left)
            l.append(root.val)
        
            if root.right:
                inorder(root.right)
            return l    
        return inorder(root)