f = 1853124397
p = 907
real = 2 ** f
sf = real % p
n = real // p
pn = p * n
print(f, p, sf)

word = "nto-"
oup = ''
for i in range(len(word)):
    c = ord(word[i])
    c_bin = str(bin(c))[2:]
    c_bin = "0" * (8 - len(c_bin)) + c_bin
    oup += c_bin
    print(c_bin, end='')
print()
print(int(oup, 2))

cur_bin = oup
# print(cur, cur_bin)
for j in range(0, len(cur_bin), 8):
    symbol = cur_bin[j: j+8]
    # print(symbol)
    print(chr(int(symbol, 2)), end='')
print()
