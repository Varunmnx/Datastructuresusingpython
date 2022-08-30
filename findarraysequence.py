def findarrayseq(parent,child):
  d=0
  for i in range(parent.length):
    if parent[i] == child[d]:
      d+=1
    if d== child.length:
      return true
