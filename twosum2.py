
class findme:
 def __init__(self,target =None):
     self.target =target   
 def finder(self) :
     val = self.target
     l1= [1,2,3,4,5,1,3,4]
     start = 0
     end = len(l1) -1
     while start< end:
       if l1[start] +l1[end] == val:
           return [start,end]
       elif l1[start] +l1[end] > val:
           end -=1
       elif l1[start] +l1[end] < val:
           start +=1
if __name__ =="__main__":
    f = findme(10)
    v =f.finder()
    print(v)