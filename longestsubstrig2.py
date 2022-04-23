track ={}
curlen =0
start = 0
length =0
s ="abcdbcdefgh" 
for i,letter in enumerate(s):
    if letter in track and track[letter] >= start:
        start = track[letter] +1
        curlen = i- track[letter]
        track[letter] = i
    else:
        track[letter] =i
        curlen += 1
        if curlen> length:
            length = curlen
print(length)    

