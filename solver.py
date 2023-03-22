# 100000000000000000000000000000000000000000000 X
#                         101010000111100100010 p
#                           1000101010100010101 c
#  11111111111111111111111001011011010100101010 n * p
#
#
# 101111010101001111111111111111111111111111111111111...
#
# 101113311231131123111110101010
#
# 101010111010
# zxcvbnmjhgfdcvbnmjhgfcx
# 101010111010
#   101010111010
#    101011000101
# n * p + c = X

from math import log


# f = 54
# p = 47
# real = 2 ** f
# sf = real % p
# n = real // p
# print(f, p, sf, n)

# f = 13
# p = 59
# real = 2 ** f
# sf = real % p
# n = real // p
# pn = p * n
# print(f, p, sf, n, pn)

# f = 13
from pip._vendor.progress import counter

p = 907  # 59
# real = 2 ** f
sf = 385  # 50
# n = real // p
# pn = p * n
print(p, sf)

# f_bin = str(bin(f))[2:]
p_bin = str(bin(p))[2:]
# real_bin = str(bin(real))[2:]
sf_bin = str(bin(sf))[2:]
# n_bin = str(bin(n))[2:]
# pn_bin = str(bin(pn))[2:]
print(p_bin, sf_bin)
# print(real_bin)

def i2b(i):
    return str(bin(i))[2:]

def s2m(s):
    m = []
    for i in range(len(s)):
        m.append(s[i])
    return m

# f_mass = s2m(f_bin)
p_mass = s2m(p_bin)
# r_mass = s2m(real_bin)
sf_mass = s2m(sf_bin)
# n_mass = s2m(n_bin)
# pn_mass = s2m(pn_bin)

min_flag = len(p_bin)
check_real = 2 ** min_flag
print(i2b(check_real))
start_pn = check_real - sf
start_pn_bin = i2b(start_pn)
start_pn_mass = s2m(start_pn_bin)
print(start_pn_mass)
start_pn_mass.reverse()
print(start_pn_mass)
while len(start_pn_mass) < len(p_bin):
    start_pn_mass.append('0')
print(start_pn_mass)

buffer = p_mass.copy()
buffer.reverse()
for i in range(len(buffer)):
    buffer[i] = int(buffer[i])

pr = p_mass.copy()
pr.reverse()
i = 0
ansewer = ''
counter = 0
ans = []
while True:
    if not(i < len(buffer) - 1 or buffer[i] != 1):
        print("OK", *buffer, ansewer)

        counter += 1
        maybe = 0
        b = 1
        step = 2
        for i in buffer:
            if i == 1:
                maybe += b
            b *= 2
        # print(maybe, str(bin(maybe)))
        # print(sf_bin)

        real_found = maybe + sf
        # print(real_found, i2b(real_found))
        flag_found = log(real_found, 2)
        print(flag_found)
        ans.append(int(flag_found))

        if counter > 3:
            if ans[2] - ans[1] == ans[1] - ans[0] == ans[3] - ans[2]:
                print("Validated delta", ans[1] - ans[0])
                print("Seed", ans[0])
            else:
                print("Not validated values", *ans)
            break

        buffer.append(0)


    # print(buffer, ansewer)
    if i < len(start_pn_mass):
        if buffer[i] % 2 == int(start_pn_mass[i]):
            if i < len(buffer) - 1:
                buffer[i+1] += buffer[i] // 2
            else:
                buffer.append(buffer[i]//2)
            buffer[i] = buffer[i] % 2
            ansewer += '0'
        else:
            for j in range((len(pr) - 1) - (len(buffer) - i - 1)):
                buffer.append(0)
            for j in range(i, i + len(pr)):
                buffer[j] += int(pr[j-i])

            if i < len(buffer) - 1:
                buffer[i+1] += buffer[i] // 2
            else:
                buffer.append(buffer[i]//2)
            buffer[i] = buffer[i] % 2
            ansewer += '1'
    else:
        if buffer[i] % 2 == 1:
            if i < len(buffer) - 1:
                buffer[i+1] += buffer[i] // 2
            else:
                buffer.append(buffer[i]//2)
            buffer[i] = buffer[i] % 2
            ansewer += '0'
        else:
            for j in range((len(pr) - 1) - (len(buffer) - i - 1)):
                buffer.append(0)
            for j in range(i, i + len(pr)):
                buffer[j] += int(pr[j-i])

            if i < len(buffer) - 1:
                buffer[i+1] += buffer[i] // 2
            else:
                buffer.append(buffer[i]//2)
            buffer[i] = buffer[i] % 2
            ansewer += '1'
    i += 1
# print("OK", *buffer, ansewer)
#
# maybe = 0
# b = 1
# step = 2
# for i in buffer:
#     if i == 1:
#         maybe += b
#     b *= 2
# print(maybe, str(bin(maybe)))
# print(sf_bin)
#
# real_found = maybe + sf
# print(real_found, i2b(real_found))
# flag_found = log(real_found, 2)
# print(flag_found)

cur = ans[0]
delta = ans[1] - ans[0]
print("Variants:")

for i in range(10000000):
    cur_bin = str(bin(cur))[2:]
    cur_bin = '0' * (8 - (len(cur_bin) % 8)) + cur_bin
    word = ''
    # print(cur, end='   ')
    for j in range(0, len(cur_bin), 8):
        symbol = cur_bin[j: j+8]
        # print(symbol)
        # print(chr(int(symbol, 2)), end='')
        word += chr(int(symbol, 2))
    # print()
    if word[:3] == 'nto':
        print(cur, word)
    cur += delta
