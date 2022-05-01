class TreeNode:
    def __init__(self,data) :
        self.data = data
        self.children = []
        self.parent = None

    def addchildren(self,child):
         child.parent = self
         self.children.append(child)
    def printitems(self):
        print(self.data)
        if self.children:
            for child in self.children:
                child.printitems()     
if __name__ =="__main__":
   Beginning = TreeNode("The head") 
   Branch1 = TreeNode("Branch1")
   Branch2 = TreeNode("Branch2")
   Beginning.addchildren(Branch1)
   Beginning.addchildren(Branch2)
   Beginning.printitems()                