def find(paths):
 outgoing_count ={}
 for path in paths:
     citya,cityb=path
     outgoing_count[citya] = outgoing_count.get(citya,0)+1 #left side of the list got 1
     outgoing_count[cityb] = outgoing_count.get(cityb,0)  #right side of the array got 0
 for i in outgoing_count:
     if outgoing_count[i] ==0:
        return i


if __name__=="__main__":
    paths = [["london", "Newyork"], ["Newyork", "Lisma"], ["Lisma", "sao polo"]]
    result = find(paths)
    print(result)









#
# for i in paths:
#     city_a,city_b = i
#     print(city_a)











