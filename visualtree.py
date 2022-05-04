class TreeNode:
    def __init__(self,val):
        self.val = val
        self.children = []
        self.parent =None

    def addchild(self,child):
        self.parent = self
        self.children.append(child)

    def level(self):
        p = self.parent
        l = 0
        while p:
            l += 1
            p = p.parent
        return l
    def outputtree(self):
        spaces =''*self.level()*2
        print(spaces + self.val)
        if self.children:
            for ch in self.children:
                ch.outputtree()



if __name__ == "__main__":
    main = TreeNode("DAD")
    son1 = TreeNode("son1")
    son1.addchild(TreeNode("sonofson1"))
    son1.addchild(TreeNode("sonofson2"))
    son2 = TreeNode("son2")
    son2.addchild(TreeNode("sonofson2"))
    son2.addchild(TreeNode("sonofson2"))
    main.addchild(son1)
    main.addchild(son2)
    main.outputtree()
