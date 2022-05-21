class Btree:
    def __init__(self,val):
        self.val = val
        self.left =None
        self.right =None
    def insert(self,data):
        if self.val:
            if data<self.val:
                if not self.left:
                    self.left = Btree(data)
                else:
                    self.left.insert(data) 

            if data<self.val:
                if not self.right:
                    self.right = Btree(data)
                else:
                    self.right.insert(data)
        else:
            self.val = Btree(data)             
    def maximum_depth(self,root):
                 if not root:
                     return 0
                 return (1+ max(self.maximum_depth(root.left),self.maximum_depth(root.right)))       # one function returns 0+1 first


if __name__ =="__main__":
   Root = Btree(100)
   Root.left =Btree(90)
   Root.right =Btree(110)
   Root.insert(111)
   Root.insert(55)
   Root.insert(26)
   Root.insert(18)
   print(Root.maximum_depth(Root))

   """
      10
     / \
    9    30
   /     /\     
  8     4
 /
7 
   """