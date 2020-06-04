from collections import deque

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#Cria uma fila a partir da lista
fila = deque(lista)
#Insere no início da fila
fila.appendleft(32)
print(fila)

#Insere no final da lista
fila.append(57)
print(fila)

#troca a posição do útimo elemento da lista com o elemento do índice passado
fila.rotate(0)
print(fila)