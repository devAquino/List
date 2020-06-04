lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lista)

print()
#Acessando o elemento da lista pela posição
print('primeiro elemento da lista ->', lista[0])
print('quarto elemento da lista ->', lista[3])
print("ultimo elemento da lista ->", lista[-1])

#Retorna uma nova lista com elementos a partir do segundo
print(lista[2:])
print()

#Cria uma cópia da lista
lista1 = lista[:]
#Cria uma cópia da lista
lista2 = lista.copy()
#Invertendo a lista
lista1.reverse()
print(lista1)

k = 0
for l in lista:
    print(k,'->',l)
    k += 1