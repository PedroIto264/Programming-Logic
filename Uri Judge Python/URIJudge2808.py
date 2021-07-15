i, d = input().split()
c = abs(ord(i[0]) - ord(d[0]))
l = abs(int(i[1]) - int(d[1]))

if (c == 1 and l == 2) or (c == 2 and l == 1):
    print('VALIDO')
else:
    print('INVALIDO')