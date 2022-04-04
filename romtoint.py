l ={"I":1,
    "V":5,
    "X":10,
    "L":50,
    "C":100,
    "D":500,
    "M":1000,
     }
# stringv = "CD"
# num = 0
# last ="I"
# for numerical in stringv[::-1] :   #DL
#     if l[numerical] < l[last]:     # first condition is dummy checks with 1 if its less than .
#         num -= l[numerical]
#     else:
#         num += l[numerical]
#     last = numerical
# print(num)
# 500<1 no so +500  100<500 yes 500 -100













stri = "DXM"
anw =0
last = "I" # lowestt value is taken 
for i in stri[::-1]:
    if l[i] < l[last]:
        anw -= l[i]
    else:
        anw += l[i]
    last = i
print(anw)















