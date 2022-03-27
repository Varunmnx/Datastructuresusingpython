class Alloperationsforstring:
    def __init__(self) :
        print("HAPPY STRINGY")
    def reversing2(self,stringon):
        b =0
        end =len(stringon)-1
        temp = chr
        while b<end:
            temp = stringon[b]
            stringon[b] = stringon[end]
            stringon[end] = temp
            b +=1
            end -= 1
        print(stringon)

if __name__ =="__main__":
    s = Alloperationsforstring()
    stringon = input("enter list of characters :").split()
    print("your input was {}".format(stringon))
    s.reversing2(stringon)            

            
        