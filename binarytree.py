class BTNode:
    def __init__(self, val):
      self.leftNode = None
      self.rightNode = None
      self.val = val
    def insertNode(self, val):
        if self.val:
        if val < self.val:
            if self.leftNode is None:
                self.leftNode = BTNode(val)
        else:
                self.leftNode.insertNode(val)
        elif val > self.val:
            if self.rightNode is None:
            self.rightNode = BTNode(val)
            else:
            self.rightNode.insertNode(val)
        else:
            self.val = val
def searchVal(self, data):
   if data < self.val:
    if self.leftNode is None:
       return str(data)+" is not Found in the Binary Tree"
    return self.leftNode.searchVal(data)
   elif data > self.val:
     if self.rightNode is None:
        return str(data)+" is not Found in the Binary Tree"
     return self.rightNode.searchVal(data)
   else:
     return str(self.val) + " is found in the Binary Tree"
root = BTNode('A')
root.insertNode('B')
root.insertNode('C')
root.insertNode('D')
root.insertNode('E')
root.insertNode('F')
print(root.searchVal('B'))
print(root.searchVal('b'))
print(root.searchVal('D'))