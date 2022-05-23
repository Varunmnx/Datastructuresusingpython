def convert(s,num):
    if num==1:
        return s
    temp =[[] for i in range(num)] #for creating 4 arrays in an array to perform dimentional arranging
    count=0
    TurnBack =False # to append the next element in the previous array
    for i in s:
        temp[count].append(i)
        if not TurnBack:
            if count ==num-1:
                TurnBack =not TurnBack
                count-=1
            else:
                count+=1
        else:
            if count == 0:
                TurnBack = not TurnBack
                count+=1
            else:
                count-=1
    pp=""
    for j in temp:
        pp+="".join(j)
    print(pp)

if __name__=="__main__":
 convert("FLIPCARTISHIRING",4)
