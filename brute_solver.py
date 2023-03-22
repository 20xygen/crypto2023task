from math import log
p = 1332179293327198840020823060356539467119090904508293337232631835620005503733906225483245077
shared = 1168754188085670347662509463389294306038240785390905722788420559649097057822642335940170569
# guess = log()
n = 1
c = p
print(log(c + shared, 2))
while True:
    n+=1
    c+=p
    th = log(c + shared, 2)
    if n % 10000000 == 0:
        print(n, th)
    if abs(int(th) - th) < 0.00001:
        if 2 ** int(th) == c + shared:
            print(th, n)
