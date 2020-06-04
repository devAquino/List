lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#Adiciona elemento ao final da lista
lista.append(14)
print(lista)
#Adiciona o elemento na posição indicada
lista.insert(3, 25)
print(lista)

#Retorna o índece base zero do primeiro intem cujo o valor é igual a 7
lista.index(7, 0, 8)
print(lista)

#Retorna a quantidade de vezes que o valor passado no parãmetro aparece na lista
contador = lista.count(4)
print(contador)

#Remove o ultimo elemento da lista
lista.pop()
print(lista)
#Remove o elemento passado, se não existir retorna um valueError
lista.remove(2)
print(lista)
#Remove todos os elementos da lista
nova_lista = lista[:]
nova_lista.clear()
print(nova_lista)

nova_lista1 = lista[:]
del nova_lista1[:]
print(nova_lista1)
