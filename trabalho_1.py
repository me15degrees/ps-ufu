#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#
#~# Maria Eduarda Nascimento Andrade ~#
#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#

L = int(input())
C = int(input())

#calcula o número de lajotas
tipo_2 = 2*(L-1) + 2*(C-1)
tipo_1 = L*C + (L-1)*(C-1)

print(tipo_1)
print(tipo_2)