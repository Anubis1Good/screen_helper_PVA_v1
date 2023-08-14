my_symbols = []
vol = []
vol_my_symbols = dict()

with open('symbols.txt','r') as fs:
    for line in fs:
        n = line.find('\n')
        # line = line[:n]
        sep = line.find(' ')
        my_symbols.append(line[:sep])
        vol.append(float(line[sep+1:n]))


i = 0
length = len(my_symbols)
while i < length:
    vol_my_symbols[my_symbols[i]] = vol[i]
    i += 1


