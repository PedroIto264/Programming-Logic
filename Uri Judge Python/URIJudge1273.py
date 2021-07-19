while True:
    nump = int(input())
    if nump == 0:
        break
    list1 = []
    maior = 0
    for j in range(nump):
        list1.append(input())
        if len(list1[j])>maior:
            maior = len(list1[j])
    for k in range(nump):
        if len(list1[k])<maior:
            print("{}".format(list1[k]).rjust(maior))
        else:
            print("{}".format(list1[k]))
print()