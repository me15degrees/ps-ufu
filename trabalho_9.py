#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#
#~# Maria Eduarda Nascimento Andrade ~#
#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#

from collections import defaultdict

def attack_ship(board, ships, attacked_positions, pos):
    letter = board[pos[0]][pos[1]]
    # adicionando a posição ao dicionário de ataque, não tem problema os ateques ao "." também estarem aqui
    attacked_positions[letter].append(pos)
    if letter == ".":
        print("agua")
    elif len(set(attacked_positions[letter])) == len(ships[letter]):
        # comparando com o len de set, pois assim sempre manterá apenas as posições únicas
        # e quando os tamanhos forem os mesmos significa que todas as posições do navio foram atacadas
        print(f"afundou o navio {letter}")
    else:
        # nesse caso, não afundou e não é um ponto, logo so resta ser um navio que foi atacado
        print(f"atingiu o navio {letter}")

    # atualiza o dict de posições atacadas para as próximas jogadas
    return attacked_positions

def convert_input(move):
    idx_line = "ABCDEFGHIJ".find(
        move[0]
    )  # converte a letra em questão para seu respectivo index
    idx_column = int(move[1]) - 1  # colunas começam com 1, mas os indexes começam em 0

    return idx_line, idx_column

def find_ships(board):
    # essa função adiciona cada posição em uma lista, na qual a lista sera o valor da chave de um dicionário
    """
    ships = {
        "A": [(0,0), (0,1)],
        "B": [(0,6)],
    }
    """
    ships = defaultdict(list)
    # o default dict foi explicado na main
    # um código equivalente está como exemplo abaixo, comentado
    for i, line in enumerate(board):
        for j, letter in enumerate(line):
            if letter != ".":
                # if letter not in ships:
                #     ships[letter] = []
                ships[letter].append((i, j))

    return ships

def main():
    board = [input().split() for _ in range(10)]  # recebe a matrix do jogo
    num_moves = int(input())  # numero de jogadas
    ships = find_ships(board)  # recebe um dicionario com cada navio e posições
    attacked_positions = defaultdict(list)
    # o default dict é um dicionario que possui um valor padão
    # por exemplo:
    # caso eu peça attacked_positions["felipe"], um dict me retornaria um erro visto que "felipe" não existe em suas keys
    # o default dict vai adicionar um valor default para esse caso, que no nosso uso sera o retorno da função list, logo uma lista vazia
    # tambem está sendo usando no "find_ships", e é util para eu poder adicionar as posições em uma lista sem ter que verificar se ela existe
    for _ in range(num_moves):
        # recebe o input e converte para indexes
        move = input().split()
        pos = convert_input(move)
        # ataca o tabuleiro e printa as respostas
        attacked_positions = attack_ship(board, ships, attacked_positions, pos)
main()
