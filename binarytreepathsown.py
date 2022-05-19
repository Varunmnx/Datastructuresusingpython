from logging import root


class Tree:
    def __init__(self,val) :
        self.val = val
        self.left = None
        self.right = None
    def inorderlist(self,Root):
        def dfs(Root,p=[],result=[]):
            if not Root:
                return
            p.append(Root.val)
            if not Root.left and not Root.right:
                    result.append('->'.join(map(str,p)))
         
            dfs(Root.left)
            dfs(Root.right) 
            p.pop()
            return result
        return dfs(Root)   

if __name__ =="__main__":
    Root = Tree(20)
    Root.left = Tree(10)
    Root.right =Tree(30)
    Root.left.right =Tree(14)
    print(Root.inorderlist(Root))
