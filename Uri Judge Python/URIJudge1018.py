valor = int(input())
notas100 = valor//100
r = valor%100
notas50 = r//50
r = r%50
notas20 = r//20
r = r%20
notas10 = r//10
r = r%10
notas5 = r//5
r = r%5
notas2 = r//2
notas1 = r%2

print(valor)
print(notas100, "nota(s) de R$ 100,00")
print(notas50, "nota(s) de R$ 50,00")
print(notas20, "nota(s) de R$ 20,00")
print(notas10, "nota(s) de R$ 10,00")
print(notas5, "nota(s) de R$ 5,00")
print(notas2, "nota(s) de R$ 2,00")
print(notas1, "nota(s) de R$ 1,00")