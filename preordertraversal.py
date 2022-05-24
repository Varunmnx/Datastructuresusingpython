# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    def trav(self,root,p):
        if(root==None):
            return
        p.append(root.val)
        self.trav(root.left,p)
        self.trav(root.right,p)
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        p=[]
        self.trav(root,p)
        return(p)