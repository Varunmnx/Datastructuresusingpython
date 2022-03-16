class Node:
   def __init__(self, dataval=None):
      self.dataval = dataval
      self.nextval = None

class SLinkedList:
   def __init__(self):
      self.headval = None

   def listprint(self):
      printval = self.headval
      while printval is not None:
         print (printval.dataval)
         printval = printval.nextval

list = SLinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

# Link first Node to second node
list.headval.nextval = e2

# Link second Node to third node
e2.nextval = e3

list.listprint()








# class Node:
#    def __init__(self,data) :
#       self.data = data
#       self.pointingtonode = None

# class Linkedlist:
#    def __init__(self) :
#       self.headvalue =None
      

# if __name__=="__main__":
#    list = Linkedlist()
#    list.headvalue = Node("mon")
#    e2 = Node("tue")
#    e3 = Node("wed")
#    e4 =Node("thur")
#    list.headvalue.pointingtonode = e2
#    e2.pointingtonode =e3
#    e3.pointingtonode = e4
   
