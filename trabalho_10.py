#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#
#~# Maria Eduarda Nascimento Andrade ~#
#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#

# recebe a entrada separa por espaço e armazena nas variáveis students e teams
students_teams = input().split()
students = int(students_teams[0])
teams = int(students_teams[1])

# cria uma lista vazia chamada l para armazenar as habilidades dos estudantes
l = []

# laço que vai appendar na lista l incialmente vazia
for i in range(students):
    student_hability = input().split()
    x = student_hability[0]  # nome do estudante
    y = int(student_hability[1])  # habilidade do estudante convertida para inteiro
    l.append((x, y))

# ordena a lista de tuplas l com base na habilidade (segundo elemento da tupla) em ordem decrescente
l_ordenated = sorted(l, key=lambda x: x[1], reverse=True)

# cria um dicionário chamado ordenate a partir da lista ordenada de tuplas ("nome", habilidade)
ordenate = {chave: valor for chave, valor in l_ordenated}

# cria uma lista vazia chamada all_teams para armazenar os times
all_teams = []

# loop para criar os times, cada um contendo um estudante do dicionário ordenate
for i in range(teams):
    new = {chave: valor for chave, valor in list(ordenate.items())[i:i + 1]}
    all_teams.append(new)

# cria uma lista de dicionários vazios chamada empty_dicts
empty_dicts = [{} for _ in range(teams)]

# inicializa variável com zero
factor = 0

# loop para distribuir os estudantes entre os times de forma circular
for chave, valor in ordenate.items():
    all_teams[factor][chave] = valor
    # verifica se todos os times receberam um estudante, se não, passa para o próximo time
    if factor == len(all_teams) - 1:
        factor = 0
    else:
        factor += 1

# loop para imprimir os nomes dos estudantes em cada time, ordenados alfabeticamente
for idx, team in enumerate(all_teams):
    keys = sorted(list(team.keys()))  # obter as chaves do time e ordenar em ordem alfabética
    print(f"Time {idx + 1}")
    for item in keys:
        print(item)  # imprime o nome do estudante
    print()  # imprime uma linha em branco entre os times