while True:
    try:
        n = int(input())
        c = 0
        while (n > 1):
            n //= 2
            c += 1
        print(c)
    except EOFError:
        break