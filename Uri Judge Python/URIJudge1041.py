n = float(input())
x = 1
while x == 1:
    while n < 0 or n > 10:
        print("nota invalida")
        n = float(input())
    if n >= 0 and n <= 10:
        n2 = float(input())
        while n2 < 0 or n2 > 10:
            print("nota invalida")
            n2 = float(input())
        soma = (n + n2)/2
        print("media = {:.2f}".format(soma))
        print("novo calculo (1-sim 2-nao)")
        x = int(input())
        if x != 2 and x != 1:
            while x != 1 and x !=2:
                print("novo calculo (1-sim 2-nao)")
                x = int(input())
    if x == 1:
        n = float(input())
    else:
        break