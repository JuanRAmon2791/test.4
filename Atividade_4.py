# Passo 1: Insere os números [1, 2, 3, 4 e 5] em uma lista - com 5 células
lista = [1, 2, 3, 4, 5]

# Passo 2: Remove todos os dados da lista e insere-os em uma Pilha - com 5 células.
# Deve-se sempre remover os dados da célula inicial da lista
pilha = []
while len(lista) > 0:
    pilha.append(lista.pop(0))

# Passo 3: Remove os dados da Pilha e insere-os em uma Fila - com 10 células)
fila = []
while len(pilha) > 0:
    fila.append(pilha.pop())

# Passo 4: Insere os números [6, 7, 8, 9 e 10] na lista
lista.extend([6, 7, 8, 9, 10])

# Passo 5: Repete os passos 2 e 3
while len(lista) > 0:
    while len(lista) > 0:
        pilha.append(lista.pop(0))
    while len(pilha) > 0:
        fila.append(pilha.pop())

# Passo 6: Exibe todos os números que foram inseridos na fila
print(fila)
