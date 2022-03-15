class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data
   # def PrintTree(self):
   #    print(self.data)

root = Node(10)
node1 = Node(20)
node2 = Node(30)
root.left = node1
root.right = node2

print("root node is : " ,root.data)
print( f" left child node of {root.data} is  {root.left.data}")
print( f"right child node of {root.data} is {root.right.data}")