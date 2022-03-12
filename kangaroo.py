
def result(x1,x2,y1,y2):
  if x1<x2 and y1<y2:
   return "NO"
  if y1!=y2 and (x2-x1)%(y2-y1) ==0 :
   return "YES"


if __name__=="__main__":
 x1=int(input())
 x2=int(input())
 y1=int(input())
 y2=int(input())
 anw =result(x1,x2,y1,y2)
 print(anw)