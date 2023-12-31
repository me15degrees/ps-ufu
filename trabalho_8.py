#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#
#~# Maria Eduarda Nascimento Andrade ~#
#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#

def find_start_positions(matrix, word): # passa os parâmetros que serão analisados/percorridos
    result = [] # guarda o index
    for i, line in enumerate(matrix):
        for j, letter in enumerate(line):
            if letter.lower() == word[0] or letter.lower() == '*': # trata a letra e compara com a primeira letra da palavra/*
                result.append((i, j)) # adiciona as posições na lista result
    return result # retorna a lista 


def search_right(i, j, matrix, word, n_columns, upper=False): # função que faz a busca para direita
    counter = 0 # incicializa o contador
    for k, letter in enumerate(word):
        if j + k < n_columns and ( # não pode dar index error
            matrix[i][j + k].lower() == letter or matrix[i][j + k] == "*" # compara a matriz com a letra ou coringa
        ):
            if upper: # falso depois verdadeiro na segunda chamada
                matrix[i][j + k] = matrix[i][j + k].upper() # atualiza as letras compatíveis encontradas de minúsculo para maiúscula
            counter += 1 # incrementa contador
    return counter == len(word) # expressão booleana que retorna True


def search_down(i, j, matrix, word, n_lines, upper=False): # função que faz a busca para baixo
    counter = 0 # incicializa o contador
    for k, letter in enumerate(word): # não pode dar index error
        if i + k < n_lines and (
            matrix[i + k][j].lower() == letter or matrix[i + k][j] == "*" # compara a matriz com a letra ou coringa
        ):
            if upper: # falso depois verdadeiro na segunda chamada
                matrix[i + k][j] = matrix[i + k][j].upper() # atualiza as letras compatíveis encontradas de minúsculo para maiúscula
            counter += 1 # incrementa contador
    return counter == len(word) # expressão booleana que retorna True


def search_right_upper(i, j, matrix, word, n_columns, upper=False): # função que faz a busca na diagonal1
    counter = 0 # incicializa o contador
    for k, letter in enumerate(word):
        if (
            i - k >= 0 # não pode dar index error
            and j + k < n_columns
            and (matrix[i - k][j + k].lower() == letter or matrix[i - k][j + k] == "*")
        ):
            if upper: # falso depois verdadeiro na segunda chamada
                matrix[i - k][j + k] = matrix[i - k][j + k].upper()
            counter += 1 # incrementa o contador
    return counter == len(word) # expressão booleana que retorna True


def search_right_down(i, j, matrix, word, n_columns, n_lines, upper=False): # função que faz a busca na diagonal2
    counter = 0 # incicializa o contador
    for k, letter in enumerate(word):
        if (
            j + k < n_columns # não pode dar index error
            and i + k < n_lines
            and (matrix[i + k][j + k].lower() == letter or matrix[i + k][j + k] == "*")
        ):
            if upper:  # falso depois verdadeiro na segunda chamada
                matrix[i + k][j + k] = matrix[i + k][j + k].upper()
            counter += 1 # incrementa o contador
    return counter == len(word) # expressão booleana que retorna True


def search_word(matrix, word, n_lines, n_columns): # função que faz o esquema de busca
    start_positions = find_start_positions(matrix, word) # chama a função que retorna a lista de index
    equals = 0 # realiza contagem de vezes
    for i, j in start_positions: #itera em cima de start positions
        ## right
        if search_right(i, j, matrix, word, n_columns): # se for True
            equals += 1 # contabiliza mais uma ocorrência
            search_right(i, j, matrix, word, n_columns, upper=True) # chama pela segunda vez passando o parâmetro upper como True
        ## down
        if search_down(i, j, matrix, word, n_lines): # se for True
            equals += 1 # contabiliza mais uma ocorrência
            search_down(i, j, matrix, word, n_lines, upper=True) # chama pela segunda vez passando o parâmetro upper como True
        ## right upper
        if search_right_upper(i, j, matrix, word, n_columns): # se for True
            equals += 1 # contabiliza mais uma ocorrência
            search_right_upper(i, j, matrix, word, n_columns, upper=True) # chama pela segunda vez passando o parâmetro upper como True
        ## right down
        if search_right_down(i, j, matrix, word, n_columns, n_lines): # se for True
            equals += 1 # contabiliza mais uma ocorrência
            search_right_down(i, j, matrix, word, n_columns, n_lines, upper=True) # chama pela segunda vez passando o parâmetro upper como True

    return equals # retorna a quantidade de vezes em cada iteração

def main():
    num_lines = int(input())
    num_columns = int(input())

    word_matrix = [input().split() for _ in range(num_lines)]  # recebe a matriz em uma variável com um list comprehension
    words = [input() for _ in range(int(input()))] # recebe uma lista de palavras para serem buscadas no caça-palavras

    print("-" * 40)
    print("Lista de Palavras") 
    print("-" * 40)
    for word in words: # faz a sequência de prints para cada palavra da lista de palavras
        result = search_word(word_matrix, word, num_lines, num_columns) # retorna o equals pra cá
        print(f"Palavra: {word}")
        print(f"Ocorrencias: {result}")
        print("-" * 40)

    for line in word_matrix:
        print(" ".join(line)) # faz o print ficar formatado com os espaços que precisa

main()


