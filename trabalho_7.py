#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#
#~# Maria Eduarda Nascimento Andrade ~#
#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#

big_square_size = int(input()) # tamanho do lado do quadrado maior
big_square = [
    list(map(int, input().split())) for _ in range(big_square_size) # matriz que recebe input das linhas do quadrado maior
]
small_square_size = int(input()) # tamanho do lado do quadrado menor
small_square = [
    list(map(int, input().split())) for _ in range(small_square_size)  # matriz que recebe input das linhas do quadrado menor
]

max_similarity = -1 # inicializa uma variável
for line in range(big_square_size - small_square_size + 1): # itera pelas linhas do quadrado grande em que caiba o quadrado pequeno
    for column in range(big_square_size - small_square_size + 1): # itera pelas colunas do quadrado grande em que caiba o quadrado pequeno
        equals = 0 # variável que será usada para contar o número de elementos certos
        for i in range(small_square_size):# itera pelas linhas do quadrado pequeno
            for j in range(small_square_size): # itera pelas colunas do quadrado pequeno
                if big_square[line + i][column + j] == small_square[i][j]: # verifica a compatibilidade
                    equals += 1 # incrementa 
        similarity = equals / (small_square_size**2) * 100 # faz a porcentagem
        if similarity > max_similarity: # atualiza a variável de máxima
            max_similarity = similarity
            position = line, column # armazena a posição em que a variável de máxima foi encontrada


print(f"Posição: ({position[0]},{position[1]})")
print(f"Similaridade máxima: {max_similarity:.2f}%")