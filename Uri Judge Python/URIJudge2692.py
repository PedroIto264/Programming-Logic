casos,vezes = map(int,input().split())
letras=[]
letras_aux=[]
for i in range(casos):
    letra_1,letra_2 = input().split()
    letras.append(letra_1)
    letras_aux.append(letra_2)
for a in range(vezes):
    texto = input()
    texto=list(texto) 
    for j in range(len(texto)):
        for k in range(casos):
            if texto[j] == letras[k]:
                texto[j]=letras_aux[k]
   
            elif texto[j] == letras_aux[k]:
              texto[j]=letras[k]  
    for m in texto:
      print(m,end="")
    print()