class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(node, path):
            if not node:
                return
            
            path.append(str(node.val))
            
            if not node.left and not node.right:
                res.append("->".join(path))
                
            dfs(node.left, path)
            dfs(node.right, path)
            
            path.pop() #pop everything except the first node [a,node.left] pops the node.left
            
        res = []
        dfs(root, [])
        return res