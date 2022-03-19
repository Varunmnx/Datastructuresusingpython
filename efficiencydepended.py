def isok():
    pass
def finder():
    r = 1000
    l =1
    mid =0
    while l<r:
        mid= (l+r)//2
        if isok(mid):
           if not isok(mid-1) :
               return mid
           else:
              r= mid-1
        else:
            r = mid + 1

